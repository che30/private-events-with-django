
from django.http import HttpResponse
from django import forms
from django.shortcuts import render,redirect,get_object_or_404
from Accounts.models import Account, Event,Attendance
from userevents.forms import CreateEventForm
from attendance.forms  import AttendanceForm
def create_event_view(request):
  context = {}
  if request.user.is_authenticated == False:
    return redirect('login')
  if request.method == 'POST':
    form = CreateEventForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('events')
    else:
      print(form.errors)
      context['events_form'] = form
  else:
    form = CreateEventForm()
    context['events_form'] = form
  return render(request, 'userevents/new-event.html', context)
def all_events_view(request):
  if request.user.is_authenticated == False:
    return redirect('login')
  context = {}
  # unsubscribed = []
  # subscribed  = []
  current_user = Account.objects.get(pk=request.user.id)
  # attendance =  Attendance.objects.filter(account = current_user)
  events = Event.objects.all()
  context['events'] = events
  # context['subscribed'] = subscribed
  return render(request,'userevents/index.html', context)
def event_detail_view(request, event_id):
  if request.user.is_authenticated == False:
    return redirect('login')
  form = AttendanceForm()
  account_instance = Account.objects.get(pk=request.user.id)
  context = {}
  event_instance = Event.objects.get(pk = event_id)
  event_in_attendance = []
  all_attendances = Attendance.objects.all()
  if len(all_attendances) > 0:
    for attendance in all_attendances:
      if attendance.event == event_instance and attendance.account == account_instance:
        event_in_attendance.append(attendance.id)
  if len(event_in_attendance) > 0:
   attendance_instance = Attendance.objects.get(pk = event_in_attendance[0])
   context['attendance_instance'] = attendance_instance
  context['event'] = event_instance
  context['account'] = account_instance
  form.fields['account'].initial = account_instance
  form.fields['account'].widget = forms.HiddenInput()
  form.fields['event'].initial = event_instance
  form.fields['event'].widget = forms.HiddenInput()
  context['attendance_form'] = form
  
  return render(request, 'userevents/detail.html', context)


# Create your views here.
