import redis
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import FormView, TemplateView

from actions.utils import create_action
from .forms import ImageCreateForm
from .models import Image


r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


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
            create_action(request.user, 'bookmarked image', new_image)
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
        create_action(self.request.user, 'bookmarked image', new_image)
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
    total_views = r.incr(f"image:{image.id}:views")
    r.zincrby('image_ranking', 1, image.id)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': total_views})


class ImageDetailView(TemplateView):
    template_name = "images/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(Image, id=self.kwargs['id'], slug=self.kwargs['slug'])
        total_views = r.incr(f"image:{image.id}:views")
        r.zincrby('image_ranking', 1, image.id)

        context['section'] = 'images'
        context['image'] = image
        context['total_views'] = total_views

        return context


from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass

    return JsonResponse({'status': 'error'})


class ImageLikeView(LoginRequiredMixin, View):

    def post(self, request):
        image_id = request.POST.get('id')
        action = request.POST.get('action')

        if image_id and action:
            try:
                image = get_object_or_404(Image, id=image_id)
                if action == 'like':
                    image.users_like.add(request.user)
                    create_action(request.user, 'likes', image)
                else:
                    image.users_like.remove(request.user)
                return JsonResponse({'status': 'ok'})
            except Image.DoesNotExist:
                pass

        return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # If AJAX request and page out of range
            # return an empty page
            return HttpResponse('')
        # If page out of range return last page of results
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request, 'images/image/list_images.html', {'section': 'images', 'images': images})
    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})


class ImageListView(LoginRequiredMixin, View):

    def get(self, request):
        images = Image.objects.all()
        paginator = Paginator(images, 8)
        page = request.GET.get('page')
        images_only = request.GET.get('images_only')
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            images = paginator.page(1)
        except EmptyPage:
            if images_only:
                # If AJAX request and page out of range, return an empty page
                return HttpResponse('')
            # If page out of range, return the last page of results
            images = paginator.page(paginator.num_pages)
        if images_only:
            return render(request, 'images/list_images.html', {'section': 'images', 'images': images})
        return render(request, 'images/list.html', {'section': 'images', 'images': images})
