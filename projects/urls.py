from . import views
from django.urls import path
from .views import PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', views.index, name='welcome'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),

]
