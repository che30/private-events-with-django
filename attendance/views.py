from django.shortcuts import render, redirect
from attendance.forms import AttendanceForm
from Accounts.models import Attendance
# Create your views here.
def create_attendance_view(request):
  form = AttendanceForm(request.POST)
  if form.is_valid():
    account_instance = form.cleaned_data.get('account')
    event_instance = form.cleaned_data.get('event')
    new_attendance = Attendance(account = account_instance, event= event_instance)
    new_attendance.save()
  return redirect('events')
def delete_attendance_view(request):
  form = AttendanceForm(request.POST)
  if form.is_valid():
    account_instance = form.cleaned_data.get('account')
    event_instance = form.cleaned_data.get('event')
    Attendance(account = account_instance, event= event_instance).delete()
    # new_attendance.save()
  return redirect('events')