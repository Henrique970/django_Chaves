from django.shortcuts import render, redirect

from .forms import FormCadastroChave, FormCadastroUsuario
from .models import *


def home(request):
    return render(request, 'index.html')


def chaves_c(request):
    list = Chave.objects.all()
    return render(request, 'chaves_c.html', {'list': list})


def usuarios_c(request):
    list = Usuario.objects.all()
    return render(request, 'usuarios_c.html', {'list': list})


def exibir_chaves(request, id):
    chave = Chave.objects.get(id=id)

    context = {
        'chave': chave
    }
    return render(request, 'ch_esco.html', context)

def exibir_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)

    context = {
        'usuario': usuario
    }
    return render(request, 'usu_esco.html', context)


def deletar_chave(request, id):
    deletar = Chave.objects.get(id=id)
    if request.method == 'GET':
        deletar.delete()
        return redirect(chaves_c)

def alterar_chave(request, id):
    alterar = Chave.objects.get(id=id)
    form = FormCadastroChave(request.POST or None,instance=alterar)
    if form.is_valid():
        form.save()
        return redirect(chaves_c)

    return render(request, 'cadastro.html', {'form': form, 'lista_cadastro':alterar})

def deletar_usuario(request, id):
    deletar = Usuario.objects.get(id=id)
    if request.method == 'GET':
        deletar.delete()
        return redirect(usuarios_c)

def alterar_usuario(request, id):
    alterar = Usuario.objects.get(id=id)
    form = FormCadastroUsuario(request.POST or None,instance=alterar)
    if form.is_valid():
        form.save()
        return redirect(usuarios_c)
    return render(request, 'cadastro2.html', {'form': form, 'lista_cadastro':alterar})

def cadastro(request):
    form = FormCadastroChave(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'cadastro.html', {'form': form})


def cadastro2(request):
    form = FormCadastroUsuario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)

    return render(request, 'cadastro2.html', {'form': form})

def pegar(request):
    list = Chave.objects.all()
    return render(request, 'pegar_chave.html', {'list': list})

def pegarr(request, id):
    alterar = Chave.objects.get(id=id)
    form = FormCadastroChave(request.POST or None,instance=alterar)
    if form.is_valid():
        form.save()
        return redirect(usuarios_c)
    return render(request, 'cadastro.html', {'form': form, 'lista_cadastro':alterar})

#nome = Chave.nome
#def pegar(request):
    #Chave.objects.filter(nome==nome).update(disponivel=False)

