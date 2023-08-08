from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from cart.forms import CartAddProductForm
from shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


class ProductListView(TemplateView):
    template_name = "shop/product/list.html"

    def get_context_data(self, category_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

        context["category"] = category
        context["categories"] = categories
        context["products"] = products

        return context


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


class ProductDetailView(TemplateView):
    template_name = "shop/product/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        slug = self.kwargs["slug"]
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()

        context["product"] = product
        context["cart_product_form"] = cart_product_form

        return context