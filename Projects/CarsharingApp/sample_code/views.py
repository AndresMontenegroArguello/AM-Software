from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.

#404

def error404(request, exception):
	response = render_to_response('carsharing/404.html', {'message': str(exception)}, context_instance=RequestContext(request))
	response.status_code = 404
	return response

def error500(request):
	response = render_to_response('carsharing/500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response

#main

def index(request):
	all_cars = Car.objects.all()
	cities_count = Car.objects.values('city').distinct().count()
	countries_count = Car.objects.values('country').distinct().count()
	cars_count = Car.objects.all().count()
	drivers_count = CarUser.objects.all().count()
	#cities - top destinations
	barcelona_count = Car.objects.filter(city__name = "Barcelona").count()
	bsas_count = Car.objects.filter(city__name = "Buenos Aires").count()
	rio_count = Car.objects.filter(city__name = "Rio de Janeiro").count()
	miami_count = Car.objects.filter(city__name = "Miami").count()
	amsterdam_count = Car.objects.filter(city__name = "Amsterdam").count()
	saopaulo_count = Car.objects.filter(city__name = "Sao Paulo").count()
	santiago_count = Car.objects.filter(city__name = "Santiago").count()
	lima_count = Car.objects.filter(city__name = "Lima").count()

	template = loader.get_template('carsharing/index.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'all_cars': all_cars, 'car_user': car_user, 'cities_count': cities_count, 'countries_count': countries_count, 'cars_count': cars_count, 'drivers_count': drivers_count, 'barcelona_count': barcelona_count, 'bsas_count': bsas_count, 'rio_count': rio_count, 'miami_count': miami_count, 'amsterdam_count': amsterdam_count, 'saopaulo_count': saopaulo_count, 'santiago_count': santiago_count, 'lima_count': lima_count}
	else:
		print("not logged in")
		context = {'all_cars': all_cars, 'cities_count': cities_count, 'countries_count': countries_count, 'cars_count': cars_count, 'drivers_count': drivers_count, 'barcelona_count': barcelona_count, 'bsas_count': bsas_count, 'rio_count': rio_count, 'miami_count': miami_count, 'amsterdam_count': amsterdam_count, 'saopaulo_count': saopaulo_count, 'santiago_count': santiago_count, 'lima_count': lima_count }

	#return HttpResponse(template.render(context, request))
	return render(request, 'carsharing/index.html', context)

def rentals(request):
	all_cars = Car.objects.all()
	#car_pics = CarPicture.objects.all()
	#user_pics = ProfilePicture.objects.all()
	template = loader.get_template('carsharing/rentals.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'all_cars': all_cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'all_cars': all_cars,}
	return render(request, 'carsharing/rentals.html', context)

def cars(request):
	cars = Car.objects.filter(vehicleType__name='Car')
	template = loader.get_template('carsharing/cars.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'cars': cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'cars': cars,}

	return render(request, 'carsharing/cars.html', context)

def suvs(request):
	cars = Car.objects.filter(vehicleType__name='SUV')
	template = loader.get_template('carsharing/suvs.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'cars': cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'cars': cars,}
	return render(request, 'carsharing/suvs.html', context)

def trucks(request):
	cars = Car.objects.filter(vehicleType__name='Truck')
	template = loader.get_template('carsharing/trucks.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'cars': cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'cars': cars,}
	return render(request, 'carsharing/trucks.html', context)

def minivans(request):
	cars = Car.objects.filter(vehicleType__name='Minivan')
	template = loader.get_template('carsharing/minivans.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'cars': cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'cars': cars,}
	return render(request, 'carsharing/minivans.html', context)

def vans(request):
	cars = Car.objects.filter(vehicleType__name='Van')
	template = loader.get_template('carsharing/vans.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(user = user)
		print(car_user.username)
		context = {'cars': cars, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'cars': cars,}
	return render(request, 'carsharing/vans.html', context)

def detail(request, car_id):
	try:
		car = Car.objects.get(pk=car_id)
	except Car.DoesNotExist:
		raise Http404("Car does not exist.")

	car = Car.objects.get(pk=car_id)
	template = loader.get_template('carsharing/detail.html')
	if request.user.is_authenticated:
		print("logged in")
		user = request.user
		print(user)
		car_user = CarUser.objects.get(username = CarOwner.objects.get(car = car).owner.username)
		print(car_user.username)
		context = {'car': car, 'user': user, 'car_user': car_user}
	else:
		print("not logged in")
		context = {'car': car,}
	return render(request, 'carsharing/detail.html', context)

def city(request):
	pass

def profile(request, username):
	try:
		user = CarUser.objects.get(username=username)
	except CarUser.DoesNotExist:
		raise Http404("User does not exist.")

	user = request.user
	print(user)
	car_user = CarUser.objects.get(username = username)
	print(car_user.username)
	cars = car_user.getCars

	template = loader.get_template('carsharing/profile.html')
	if request.user.is_authenticated:
		print("logged in")
		context = {'user': user,'car_user': car_user, 'cars': cars}
	else:
		print("not logged in")
		context = {'user': user, 'car_user': car_user, 'cars': cars}
	return render(request, 'carsharing/profile.html', context)

def mycars(request, username):
	try:
		user = CarUser.objects.get(username=username)
	except CarUser.DoesNotExist:
		raise Http404("User does not exist.")

	user = request.user
	print(user)
	car_user = CarUser.objects.get(username = username)
	print(car_user.username)
	cars = car_user.getCars

	template = loader.get_template('carsharing/my-cars.html')
	if request.user.is_authenticated:
		print("logged in")
		context = {'user': user,'car_user': car_user, 'all_cars': cars}
		return render(request, 'carsharing/my-cars.html', context)
	else:
		#print("not logged in")
		#context = {'user': user, 'car_user': car_user, 'all_cars': cars}
		HttpResponseRedirect('/welcome/login')
	context = {'user': user,'car_user': car_user, 'all_cars': cars}
	return render(request, 'carsharing/my-cars.html', context)

def login(request):
	pass

def signUp(request):

	if request.user.is_authenticated:
		print("logged in")
		HttpResponseRedirect('/')
	else:
		print("not logged in")

	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)

		print(form.errors)

		if form.is_valid():
			#process the data in form.cleaned_data as required
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			country = form.cleaned_data['country']
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			phone = form.cleaned_data['phone']
			image = form.cleaned_data['picture']

			user = User(first_name = firstName, last_name = lastName, email = email, username = username, password = password)
			user.save()
			car_user = CarUser(user = user, firstName = user.first_name, lastName = user.last_name, country = country, email = user.email, username = user.username, phone = phone)
			car_user.save()
			login = Login(user = user, login = user.email, password = user.password)
			login.save()
			pic = ProfilePicture(user = car_user, image = image)
			pic.save()

			username = car_user.username
			#redirect to new URL
			return render(request, 'carsharing/registered.html', {'user':user})# + str(user_code))

	#if GET or any other method, create a blank form
	else:
		form = SignUpForm()

	return render(request, 'carsharing/signup.html', {'form':form})

def registered(request, username):
	user = CarUser.objects.get(username=username)

	template = loader.get_template('carsharing/registered.html')
	context = {'user': user,}
	return render(request, 'carsharing/registered.html', context)

def listYourCar(request):
	pass

def list(request):
	pass

def live(request):
	#car = Car.objects.get(pk=car_id)

	template = loader.get_template('carsharing/live.html')
	#context = {'car': car,}
	return render(request, 'carsharing/live.html')#, context)

def about(request):
	template = loader.get_template('carsharing/about.html')
	return render(request, 'carsharing/about.html')

def disclaimer(request):
	template = loader.get_template('carsharing/disclaimer.html')
	return render(request, 'carsharing/disclaimer.html')

def newCar(request):

	if request.user.is_authenticated:
		print("logged in")
		HttpResponseRedirect('/')
	else:
		print("not logged in")

	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)

		print(form.errors)

		if form.is_valid():
			#process the data in form.cleaned_data as required
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			country = Country.objects.get(name = form.cleaned_data['country'])
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			phone = form.cleaned_data['phone']
			image = form.cleaned_data['picture']

			user = User(first_name = firstName, last_name = lastName, email = email, username = username, password = password)
			user.save()
			car_user = CarUser(user = user, firstName = user.first_name, lastName = user.last_name, country = country, email = user.email, username = user.username, phone = phone)
			car_user.save()
			login = Login(user = user, login = user.email, password = user.password)
			login.save()
			pic = ProfilePicture(user = car_user, image = image)
			pic.save()

			user_code = car_user.code
			#redirect to new URL
			return render(request, 'carsharing/registered.html', {'user_code':user_code})# + str(user_code))

	#if GET or any other method, create a blank form
	else:
		form = SignUpForm()

	return render(request, 'carsharing/signup.html', {'form':form})

def registeredNewCar(request, car_id):
	user = CarUser.objects.get(pk=user_id)

	template = loader.get_template('carsharing/registered.html')
	context = {'user': user,}
	return render(request, 'carsharing/registered.html', context)

