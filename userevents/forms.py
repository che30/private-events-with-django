
from Accounts.models import Events
from django.forms import ModelForm
class CreateEventForm(ModelForm):
  class Meta:
    model = Events
    fields = ['name','description','schedule_date']
  def clean(self):
    if self.is_valid():
      name = self.cleaned_data['name']
      description = self.cleaned_data['description']
      schedule_date = self.cleaned_data['schedule_date']


