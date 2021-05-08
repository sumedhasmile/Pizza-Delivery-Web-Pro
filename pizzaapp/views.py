from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel,CustomerModel, OrderModel
from django.contrib.auth.models import User

# Create your views here.
def adminloginview(request):
	return render(request, "pizzaapp/adminloginview.html")

def authenticateadmin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)

	#user exists
	if user is not None:
		login(request,user)
		return redirect('adminhomepage')


	#user doesnt exists
	if user is None:
		messages.add_message(request,messages.ERROR, "Invalid Credentials")
		return redirect('adminloginpage')

def adminhomepageview(request):
	context = { 'pizzas': PizzaModel.objects.all()}
	return render(request,"pizzaapp/adminhomepage.html", context)

def logoutadmin(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
	# write a code to add a pizza into database

	name=request.POST['pizza']
	price=request.POST['price']
	PizzaModel( name= name, price= price).save()
	return redirect("adminhomepage")

def deletepizza(request,pizzaid):

	# delete the selected pizza details
	PizzaModel.objects.filter(id = pizzaid).delete()
	return redirect("adminhomepage")
	
def homepageview(request):
	return render(request, "pizzaapp/homepage.html")


def signupuser(request):
	# creating user for customer
	username = request.POST['username']
	password = request.POST['password']
	email = request.POST['email']
	# if user already exists
	if User.objects.filter(username = username).exists():
		messages.add_message(request,messages.ERROR, "User already exists")
		return redirect('homepage')

	# if user doesnt exists then create user
	User.objects.create_user(username= username ,password= password ,email = email).save()
	
	messages.add_message(request,messages.ERROR, "User successfully created")
	return redirect('homepage')

def userloginview(request):
	return render(request, "pizzaapp/userlogin.html")

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)
	#user exists
	if user is not None:
		login(request,user)
		return redirect('customerpage')


	#user doesnt exists
	if user is None:
		messages.add_message(request,messages.ERROR, "Invalid Credentials")
		return redirect('userloginpage')

def customerwelcomeview(request):
	if not request.user.is_authenticated:
		return redirect(request,'userloginpage')

	username= request.user
	context = {'pizzas': PizzaModel.objects.all(), 'username':username  }
	return render(request, 'pizzaapp/customerwelcome.html', context)

def userlogout(request):
	logout(request)
	return redirect('userloginpage')

def placeorder(request):
	username = request.user.username
	address = request.POST['address']
	status = "pending"
	ordereditems = ""
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		name = pizza.name
		price = pizza.price
		quantity = request.POST.get(str(pizzaid), " ")
		

		if str(quantity)!= "0" and str(quantity)!= " ":

			ordereditems = ordereditems + "Name: "  + name +" "+ "price: "  + str(int(quantity)*int(price)) +" "+ "Quantity: " + quantity
			
	
	OrderModel(username =username,  address = address, ordereditems = ordereditems, status = status).save()
	messages.add_message(request,messages.ERROR, "order is placed successfully")
	return redirect('customerpage')

def userorders(request):
	orders= OrderModel.objects.filter(username = request.user.username)
	context = {'orders': orders}
	return render(request, "pizzaapp/userorders.html", context)

def adminorders(request):
	orders = OrderModel.objects.all()
	context = {'orders': orders}
	return render(request,"pizzaapp/adminorders.html",context)

def acceptorder(request,orderpk):
	order = OrderModel.objects.filter(id = orderpk)[0]
	order.status = "Accepted"
	order.save()
	return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
	order = OrderModel.objects.filter(id = orderpk)[0]
	order.status = "Declined"
	order.save()
	return redirect(request.META['HTTP_REFERER'])



