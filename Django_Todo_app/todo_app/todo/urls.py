from django.urls import path
from . import views

urlpatterns = [
    path("",views.signup),
    path("login/",views.login_form),
    path("todo/",views.todo),
    path('edit_todo/<int:srno>',views.edit_todo,name="edit_todo"),
    path('delete_todo/<int:srno>',views.delete_todo,name="delete_todo")

]
