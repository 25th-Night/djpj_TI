from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem


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
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


class OrderCreateView(FormView):
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        form = self.get_form()
        return self.render_to_response({'cart': cart, 'form': form})

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

        cart.clear()
        return render(self.request, 'orders/created.html', {'order':order})