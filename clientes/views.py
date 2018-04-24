from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

# get_object_or_404  Secao 3, aula 19
# Tenta recuperar o objeto do form que o usuario esta tentando, se nao, devolve 404 no metodo persons_update

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


def persons_update(request, id):
	pessoa = get_object_or_404(Person, pk=id)

	# instanciar o form
	# instance = pessoa, indica que o form ja vai comecar instanciado com alguma coisa, Secao 3, aula 19 
	form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

	if form.is_valid():
		form.save()
		return redirect('persons_list')
	return render(request, 'person_form.html', {'formulario' : form})


def persons_delete(request, id):
	pessoa = get_object_or_404(Person, pk=id)

	# instanciar o form
	# instance = pessoa, indica que o form ja vai comecar instanciado com alguma coisa, Secao 3, aula 19 
	# form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)  COMENTEI AQUI Secao 3 aula 20 05:30

	if request.method == 'POST':
		pessoa.delete()
		return redirect('persons_list')
	
	return render(request, 'person_delete_confirm.html', {'pessoa' : pessoa})

	# return render(request, 'person_delete_confirm.html', {'formulario' : form}) COMENTEI AQUI Secao 3 aula 20 05:30

