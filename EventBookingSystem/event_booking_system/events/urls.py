from django.urls import path
from . import views

# urlpatterns = [
#     path('',views.event_list,name="event_list"),
#     path('event_detail/<slug:slug>/',views.event_details,name="event_detail"),
#     path('create/',views.create_event,name='create_event'),
#     path('update/<int:pk>/',views.edit_event,name='edit_event'),
#     path('delete/<int:pk>/',views.delete_event,name='delete_event'),

# ]


urlpatterns = [
    path('',views.EventListView.as_view(),name="event_list"),
    path('event/<slug:slug>/',views.EventDetailView.as_view(),name='event_detail'),
    path('create/',views.EventCreateView.as_view(),name='create_event'),
    path('edit/<int:pk>/',views.EventUpdateView.as_view(),name='edit_event'),
    path('delete/<int:pk>/',views.EventDeleteView.as_view(),name='delete_event'),

]
