from . import views
from django.urls import path
from .views import PostDetailView,

urlpatterns = [
    path('', views.index, name='welcome'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

]
