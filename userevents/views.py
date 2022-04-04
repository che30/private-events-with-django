from django.http import HttpResponse
from django.shortcuts import render,redirect
from userevents.forms import CreateEventForm
def create_event_view(request):
  context = {}
  if request.method == 'POST':
    form = CreateEventForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('events')
    else:
      context['events_form'] = form
  else:
    form = CreateEventForm()
    context['events_form'] = form
  return render(request, 'userevents/new-event.html', context)
def all_events_view(request):
  return HttpResponse("You're looking at all events page")


# Create your views here.
