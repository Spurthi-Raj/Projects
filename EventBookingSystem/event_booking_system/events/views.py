from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from . models import Event
from . forms import EventForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied



class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 3


class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event_list')

    # Add messages framework
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request,'Event created successfully')
        return super().form_valid(form)



class EventUpdateView(LoginRequiredMixin,UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'
    def get_success_url(self): 
        return reverse_lazy('event_detail', kwargs={'slug': self.object.slug})
    
    # permission check
    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if event.created_by != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')




# ----------------------Function based view----------------------------------------

# @login_required
# def event_list(request):
#     events = Event.objects.all()
#     paginator = Paginator(events,3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request,"events/event_list.html",{'page_obj':page_obj})

# @login_required
# def event_details(request,slug):
#     event = get_object_or_404(Event,slug=slug)
#     return render(request,'events/event_detail.html',{'event':event})
    

# @login_required
# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('event_list')
#     else:
#         form = EventForm()
#     return render(request,'events/create_event.html',{'form':form})


# @login_required
# def edit_event(request,pk):
#     event = get_object_or_404(Event,pk=pk)
#     if request.method == 'POST':
#         form = EventForm(request.POST,instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('event_detail',slug=event.slug)
#     else:
#         form = EventForm(instance=event)
#     return render(request,'events/edit_event.html',{'form':form})


# @login_required
# def delete_event(request,pk):
#     event = get_object_or_404(Event,pk=pk)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('event_list')
#     return redirect('event_list')

# ----------------------------------------------------------------------------------------------------------------
