from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from produits import models
from .models import Produit
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html' )
    #return HttpResponse('index')

def base(request):
    return render(request,'base.html')
def create(request):
    form_data = forms.UserRegister(request.POST or None)
    context={'formcreate':form_data}

    if form_data.is_valid():
        produit = models.Produit()
        produit.libelle = form_data.cleaned_data['libelle']
        produit.pu = form_data.cleaned_data['pu']
        produit.qte = form_data.cleaned_data['qte']
        produit.seuil = form_data.cleaned_data['seuil']
        produit.save()
        return redirect('/produits/')
    return render(request,'create.html',context)

def produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html',{"produits":produits})

def edit_prod(request , id):
    produit= get_object_or_404(Produit, id=id)
    context= {"produit":produit}
    if request.method == "POST":
        produit.libelle = request.POST['libelle']
        produit.pu = request.POST['pu']
        produit.qte = request.POST['qte']
        produit.seuil = request.POST['seuil']
        if produit.is_valid(): 
            produit.save()
            return redirect('/produits/')
    return render(request,'edit_prod.html', context)

def delete_prod(request , id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == "POST":
        produit.delete()
        return redirect('produits')
    return render(request,'delete_prod.html',{"produit":produit})
