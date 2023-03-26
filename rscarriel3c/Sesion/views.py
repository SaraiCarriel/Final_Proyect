from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect,  HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.nombre = form.cleaned_data.get('username')
            user.is_superuser = True
            user.is_staff = True 
            user.save()
            raw_password = form.cleaned_data.get('password1')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=user.username, password1=raw_password, password2=raw_password)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_request(request):

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			usuario = form.cleaned_data.get('username')
			contraseña = form.cleaned_data.get('password')
			user= authenticate(username=usuario, password=contraseña)

			if user is not None:
				login(request,user)
				messages.info(request, f"Bienvenido")
				return redirect("index.html")

			else:
				messages.error(request,"Usuaio o contraseña incorrecta")

		else: 
			messages.error(request,"Usuaio o contraseña incorrecta")

	form = AuthenticationForm()
	return render(request, "login.html", {"form": form})

def logout_request(request):
	logout(request)
	messages.info(request,"sesion expirada")
	return redirect("login.html")
