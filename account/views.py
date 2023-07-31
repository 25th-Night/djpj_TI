from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
#
#
# class LoginView(FormView):
#     template_name = "account/login.html"
#     form_class = LoginForm
#
#     def form_valid(self, form):
#         cd = form.cleaned_data
#         user = authenticate(self.request,
#                             username=cd['username'], password=cd['password'])
#         if user is not None:
#             if user.is_active:
#                 login(self.request, user)
#                 return HttpResponse('Authenticated successfully')
#             else:
#                 return HttpResponse('Disable account')
#         else:
#             return HttpResponse('Invalid login')
#
#
# def user_logout(request):
#     logout(request)
#     return render(request, 'account/logged_out.html')
#
#
# class LogoutView(View):
#
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return render(request, 'account/logged_out.html')
#
#
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # 새로운 사용자 객체를 생성하지만 아직 저장하지는 않습니다.
#             new_user = user_form.save(commit=False)
#             # 선택한 비밀번호를 설정합니다.
#             new_user.set_password(
#                 user_form.cleaned_data['password'])
#             # 사용자 객체를 저장합니다.
#             new_user.save()
#             # 사용자 프로필을 생성합니다.
#             Profile.objects.create(user=new_user)
#             return render(request,
#                             'account/register_done.html',
#                             {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request,
#                     'account/register.html',
#                     {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
                                        instance=request.user.profile,
                                        data=request.POST,
                                        files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                    'account/edit.html',
                    {'user_form': user_form,
                    'profile_form': profile_form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


class RegisterView(FormView):
    template_name = "account/register.html"
    form_class = UserRegistrationForm
    success_url = "account/register_done.html"

    def form_valid(self, form):
        cd = form.cleaned_data
        new_user = form.save(commit=False)
        new_user.set_password(cd['password'])
        new_user.save()
        Profile.objects.create(user=new_user)
        return render(self.request, self.get_success_url(), {'new_user': new_user})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = context.get('form')
        return context

    def get_success_url(self):
        return self.success_url


class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class ProfileEditView(LoginRequiredMixin, FormView):
    template_name = 'account/edit.html'
    form_class = UserEditForm
    profile_form_class = ProfileEditForm
    success_url = reverse_lazy('edit')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        user_form = form_class(instance=self.request.user)
        profile_form = self.profile_form_class(instance=self.request.user.profile)
        return user_form, profile_form

    def form_valid(self, form):
        user_form, profile_form = form
        user_form.save()
        profile_form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_form, profile_form = self.get_form()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context