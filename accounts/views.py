from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .form import CreateUserForm
from store.utils import cookieCart, cartData, guestOrder
from .decorators import unauthenticated_user #allowed_users, admin_only


@unauthenticated_user
def signupPage(request):

	data = cartData(request)
	cartItems = data['cartItems']
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form, 'cartItems':cartItems}
	return render(request, 'registration/signup.html', context)

@unauthenticated_user
def loginPage(request):
	
	data = cartData(request)
	cartItems = data['cartItems']
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {'cartItems':cartItems}
	return render(request, 'registration/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')