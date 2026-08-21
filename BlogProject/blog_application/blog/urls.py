from django.urls import path
from . import views

urlpatterns = [
    # we will add routes here
    path('signup/',views.signup,name='signup'),
    path('',views.post_list,name='post_list'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('create/',views.create_post,name='create_post'),
    path('edit/<int:pk>/',views.edit_post,name='edit_post'),
    path('delete/<int:pk>/',views.delete_post,name='delete_post'),


]