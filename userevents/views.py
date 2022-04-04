
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from Accounts.models import Account, Event
from userevents.forms import CreateEventForm
def create_event_view(request):
  context = {}
  if request.user.is_authenticated == False:
    return redirect('login')
  if request.method == 'POST':
    form = CreateEventForm(request.POST)
    form.clean
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
  context = {}
  events = Event.objects.all()
  context['events'] = events
  return render(request,'userevents/index.html', context)
def event_detail_view(request, event_id):
  context = {}
  event = get_object_or_404(Event, pk=event_id)
  context['event'] = event
  return render(request, 'userevents/detail.html', context)


# Create your views here.
