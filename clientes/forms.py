from django.forms import ModelForm
from .models import Person
# Person e o Model desse meu Model Form


class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']