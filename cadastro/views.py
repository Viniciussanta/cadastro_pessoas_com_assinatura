import hashlib
import base64
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from validate_docbr import CPF
from django.core.files.base import ContentFile

def home(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cpf =  request.POST.get('cpf')
        email = request.POST.get('email')
        dados_assinatura = request.POST.get('dados_assinatura')
        
        cpf_validador = CPF()
        if not cpf_validador.validate(cpf):
            return HttpResponse("Erro: esse cpf e invalidado")
        if Pessoa.objects.filter(cpf=cpf).exists():
            return HttpResponse("Erro: Esse CPF já está cadastrado!")   
        
        format, imgstr = dados_assinatura.split(';base64,')
        ext = format.split('/')[-1]
        
        arquivo_imagem = ContentFile(base64.b64decode(imgstr), name=f"{cpf}_assinatura.{ext}")
        
        sha256 = hashlib.sha256()
        for pedaco in arquivo_imagem.chunks():
            sha256.update(pedaco)
        hash_calculado = sha256.hexdigest()
        
        nova_pessoa = Pessoa()
        nova_pessoa.nome = nome
        nova_pessoa.cpf = cpf
        nova_pessoa.email = email
        nova_pessoa.assinatura_valida = True
        nova_pessoa.hash_integridade = hash_calculado
        nova_pessoa.imagem_assinatura = arquivo_imagem
        nova_pessoa.save()
        
        return HttpResponse("Cadastro realizado com sucesso! Hash: " + hash_calculado)
        
        



