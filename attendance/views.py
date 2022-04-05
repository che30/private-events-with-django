from django.shortcuts import render, redirect
from attendance.forms import AttendanceForm
from Accounts.models import Attendance
# Create your views here.
def create_attendance_view(request):
  if request.user.is_authenticated == False:
    return redirect('login')
  form = AttendanceForm(request.POST)
  if form.is_valid():
    account_instance = form.cleaned_data.get('account')
    event_instance = form.cleaned_data.get('event')
    new_attendance = Attendance(account = account_instance, event= event_instance)
    new_attendance.save()
  return redirect('events')
def delete_attendance_view(request):
  if request.method == 'POST':
    uid = request.user.id
    eid = int(request.POST.get('event'))
    Attendance.objects.filter(account_id = uid, event_id = eid).delete()
  return redirect('events')