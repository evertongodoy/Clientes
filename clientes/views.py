from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.

def persons_list(request):
	persons = Person.objects.all()
	return render(request, 'person.html', {'pessoas': persons})

# Caso o usuario tenha preenchido o formulario, usa ele, se nao, usa um form vazio
def persons_new(request):
	form = PersonForm(request.POST, request.FILES, None)

	if form.is_valid():
		form.save()
		return redirect('persons_list')
	return render(request, 'person_form.html', {'formulario' : form})