from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	#return HttpResponse('Oi Everton')

	return render(request, 'index.html')


def articles(request, year):
	return HttpResponse('O ano enviado foi ' + str(year))

def lerDoBanco(nome):
	lista_nomes = [
        {'nome': 'Ana', 'idade': 489},
        {'nome': 'Everton', 'idade': 33},
        {'nome': 'Maria', 'idade': 54},
        {'nome': 'Joao', 'idade': 21}
	]

	for pessoa in lista_nomes:
	    if pessoa['nome'] == nome:
		    return  pessoa
	else:
		    return {'nome': 'Nao encontrado', 'idade': 0 }


def fname(request, nome):
	result = lerDoBanco(nome)
	if result['idade'] > 0:
	    return HttpResponse('A pessoa foi encontrada e tem ' + str(result['idade']) + ' anos')
	else:
		return HttpResponse('Pessoa nao econtrada')


def fname2(request, nome):
	idade = lerDoBanco(nome)['idade']
	return render(request, 'pessoa.html', {'v_idade': idade})