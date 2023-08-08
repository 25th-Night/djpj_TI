from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import FormView, DetailView

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