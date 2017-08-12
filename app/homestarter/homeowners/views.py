from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.isValid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			# Manually authenticate user
			user = authenticate(username = username, password = password)
			login(request, user)
			# Redirect the user to the login page
			return redirect(login)
		else:
			form = UserCreationForm()
	return render(request, 'signup.html', {'form':form})

def login(request):
	return HttpResponse("Login page -- testing")
			