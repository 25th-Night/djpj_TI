from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # 이전 로그인 URL 패턴
    # path('login/', views.user_login, name='login'),
    # path('login/', views.LoginView.as_view(), name='login'),

    # 새로운 로그인 / 로그아웃 URL 패턴
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    # 비밀번호 변경 URL 패턴
    path('password-change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    path('', views.dashboard, name='dashboard'),

    # 배밀번호 초기화 URL 패턴
    path('password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('password-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('', views.dashboard, name='dashboard'),
]