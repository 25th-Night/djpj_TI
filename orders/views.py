from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem

from .tasks import order_created

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


class OrderCreateView(FormView):
    form_class = OrderCreateForm
    template_name = 'orders/create.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = self.get_form()
        return render(request, self.template_name, {'cart': cart, 'form': form})

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )

        # clear the cart
        cart.clear()
        # launch asynchronous task
        order_created.delay(order.id)
        # set the order in the session
        self.request.session['order_id'] = order.id
        # redirect for payment
        return redirect(reverse('payment:process'))