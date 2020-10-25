from . import views
from django.urls import path
from .views import PostDetailView, PostCreateView

urlpatterns = [
    path('', views.index, name='welcome'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new-post'),

]
