from django.urls import path
from . import views

urlpatterns = [
    path('classes/',views.list_classes ),
    path('book/',views.book_classes),
    path('booking/',views.get_booking)
]
