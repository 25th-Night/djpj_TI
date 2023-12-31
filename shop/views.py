from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from cart.forms import CartAddProductForm
from shop.models import Category, Product
from shop.recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
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
            language = self.request.LANGUAGE_CODE
            category = get_object_or_404(Category,
                                         translations__language_code=language,
                                         translations__slug=category_slug)

        context["category"] = category
        context["categories"] = categories
        context["products"] = products

        return context


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products
                   }
                )


class ProductDetailView(TemplateView):
    template_name = "shop/product/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs["id"]
        slug = self.kwargs["slug"]
        language = self.request.LANGUAGE_CODE
        product = get_object_or_404(Product,
                                    id=id,
                                    translations__language_code=language,
                                    translations__slug=slug,
                                    available=True)
        cart_product_form = CartAddProductForm()
        r = Recommender()
        recommended_products = r.suggest_products_for([product], 4)

        context["product"] = product
        context["cart_product_form"] = cart_product_form
        context["recommended_products"] = recommended_products

        return context