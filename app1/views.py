from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AutoProizvodjacModelForm, AutoModelModelForm, SignUpForm
from .models import AutoProizvodjac, AutoModel
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from .decorators import admin_access, staff_access, nonStaff_access
# Create your views here.

#@login_required
def welcome(request):
	return render(request,"welcome.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def search(request):

	query=request.GET.get('q')
	
	if query:

		
		model = AutoModel.objects.filter(Q(tip__contains=query))
		marka = AutoProizvodjac.objects.filter(Q(ime__contains=query))
		if marka:
			auto=AutoProizvodjac.objects.get(ime__contains=query)
			auto_id=auto.id
			model = AutoModel.objects.filter(automobili_id=auto_id)
			results1 = marka
			results2 = model
			return render(request,'search.html',{'Results1':results1,"Results2":results2})
		elif model:
			marka = AutoProizvodjac.objects.filter(automodel__tip__contains=query)	
			r = list(marka[:1])
			results3 = r
			results4 = model
			return render(request,'search.html',{"Results4":results4, "Results3":results3})
		else:
			results = chain(marka,model)
			return render(request,'search.html',{'Results':results})
	else:

		return render(request,'search.html')
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('welcome')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@admin_access()
def AutoProiz(request):

	if request.method == 'GET':
		form = AutoProizvodjacModelForm()
	elif request.method == 'POST':
		form = AutoProizvodjacModelForm(request.POST) 
		if form.is_valid():
			form.save()	
			svi_proizvodjaci = AutoProizvodjac.objects.all()
			return render(request, 'ispisi.html', {'Automobili':svi_proizvodjaci})
	return render(request, 'unesi_auto.html', {'form': form})

@admin_access()
def AutoMod(request):
	
	if request.method == 'GET':
		form = AutoModelModelForm()
	elif request.method == 'POST':
		form = AutoModelModelForm(request.POST) 
		if form.is_valid():
			form.save()	
			return redirect('ispisi')
	return render(request, 'unesi_auto.html', {'form': form})

@staff_access()
def ispisi_proizvodjace(request):
	svi_proizvodjaci = AutoProizvodjac.objects.all()
	return render(request, 'ispisi.html', {'Automobili':svi_proizvodjaci})

@staff_access()
def ispisi_modele(request, id):
	model =AutoModel.objects.filter(automobili_id=id)
	return render(request, 'ispisi_modele.html', {'Modeli':model})

@staff_access()	
def update_proizvodjac(request, id):
	proizvodjac =AutoProizvodjac.objects.filter(pk=id).last()
	if request.method == 'GET':		
		form = AutoProizvodjacModelForm(instance=proizvodjac)
	elif request.method == 'POST':
		form = AutoProizvodjacModelForm(request.POST, instance=proizvodjac) 
		if form.is_valid(): 
			form.save()
			return render(request, 'success.html')
	context = {'form': form}
	return render(request, 'update_proiz.html', context)

@staff_access()
def update_model(request, id):
	model =AutoModel.objects.filter(pk=id).last()
	if request.method == 'GET':		
		form = AutoModelModelForm(instance=model)
	elif request.method == 'POST':
		form = AutoModelModelForm(request.POST, instance=model) 
		if form.is_valid(): 
			form.save()
			return render(request, 'success.html')
	context = {'form': form}
	return render(request, 'update_mod.html', context)

@admin_access()
def del_proizvodjac(request, id):

	proizvodac = AutoProizvodjac.objects.filter(pk=id).last().delete()

	return render(request, 'delete.html')
@admin_access()
def del_model(request, id):

	model = AutoModel.objects.filter(pk=id).delete()

	return redirect('ispisi')

