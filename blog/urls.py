from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Post_Listview.as_view(), name='post_list'),
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/', views.Post_DetailView.as_view(),name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]