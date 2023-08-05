from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView, TemplateView

from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/create.html', {'section': 'images', 'form': form})


class ImageCreateView(LoginRequiredMixin, FormView):
    template_name ='images/create.html'
    form_class = ImageCreateForm

    def form_valid(self, form):
        # form data is valid
        cd = form.cleaned_data
        new_image = form.save(commit=False)
        # assign current user to the item
        new_image.user = self.request.user
        new_image.save()
        messages.success(self.request, 'Image added successfully')
        # redirect to new created item detail view
        return redirect(new_image.get_absolute_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.request.GET
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'images'
        return context


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


class ImageDetailView(TemplateView):
    template_name = "images/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(Image, id=self.kwargs['id'], slug=self.kwargs['slug'])

        context['section'] = 'images'
        context['image'] = image
