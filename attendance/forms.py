from django.forms import ModelForm
from django import forms
from Accounts.models import Attendance
class AttendanceForm(ModelForm):
  class Meta:
    model = Attendance
    fields = ('account', 'event')