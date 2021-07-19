from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user_view, user_profile_view, UserPostListView

urlpatterns = [
    path('register/', register_user_view, name='user-registration'),
    path('profile/<str:username>', UserPostListView.as_view(), name='user-profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]