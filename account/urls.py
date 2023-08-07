from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    # 이전 로그인 / 로그아웃 URL 패턴
    # path('login/', views.user_login, name='login'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    # path('register/', views.register, name='register'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('edit/', views.edit, name='edit'),
    path('edit/', views.ProfileEditView.as_view(), name='edit'),
    # path('users/', views.user_list, name='user_list'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/follow/', views.UserFollowView.as_view(), name='user_follow'),
    # path('users/<username>/', views.user_detail, name='user_detail'),
    path('users/<username>/', views.UserDetailView.as_view(), name='user_detail'),

]