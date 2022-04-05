from django import forms 
from Accounts.models import Attendance
class AttendanceForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ('account', 'event')