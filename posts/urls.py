from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('post/create', PostCreateView.as_view() , name='post-create'),
    path('post/details/<str:pk>', PostDetailView.as_view() , name='post-details'),
    path('post/update/<str:pk>', PostUpdateView.as_view(), name='post-update'),
    path('covid/', covid_view, name='covid'),
]