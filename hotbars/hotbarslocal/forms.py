from django.forms import ModelForm
from models import Bar, Drink

class BarForm(ModelForm):
  class Meta:
    model = Bar
    exclude = ('user', 'url')

class DrinkForm(ModelForm):
  class Meta:
    model = Drink
    exclude = ('user', 'bar')