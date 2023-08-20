from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import FormView, DetailView

from coupons.forms import CouponApplyForm
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


# class CartAddView(View):
#
#     def post(self, request, product_id):
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)
#         form = CartAddProductForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
#         return redirect('cart:cart_detail')


class CartAddView(FormView):
    form_class = CartAddProductForm

    def form_valid(self, form):
        cart = Cart(self.request)
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


class CartRemoveView(View):

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                        'quantity': item['quantity'],
                                        'override': True})
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})


class CartDetailView(DetailView):
    model = Cart
    template_name = "cart/detail.html"

    def get_object(self, queryset=None):
        return self.model(self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.object
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                'quantity': item['quantity'],
                'override': True})
        coupon_apply_form = CouponApplyForm()
        context.update({
            'cart': cart,
            'coupon_apply_form': coupon_apply_form
        })
        return context