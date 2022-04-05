
from Accounts.models import Event
from django.forms import ModelForm
from django import forms
class CreateEventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['name','description','schedule_date']
  def clean(self):
    if self.is_valid():
      name = self.cleaned_data['name']
      description = self.cleaned_data['description']
      if len(name) > 32 or len(description) > 300:
        raise  forms.ValidationError("Description Length must be less than 300,name length must be less than 5")
    else:
       raise  forms.ValidationError("Description Length must be less than 300,name length must be less than 5")
       
