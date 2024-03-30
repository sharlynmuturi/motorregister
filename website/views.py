from django.shortcuts import render, redirect
from .models import motordetail
from .forms import motordetailForm
from django.contrib import messages

# Create your views here.
def home(request):
	all_motor = motordetail.objects.all
	return render(request, 'home.html', {'all':all_motor})
	
def join(request):
	if request.method == "POST":
		form = motordetailForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Record Submitted Successfully!'))
			return redirect('home')
			
		else:
			regno = request.POST['regno']
			firstname = request.POST['firstname']
			middlename = request.POST['middlename']
			lastname = request.POST['lastname']
			staffno = request.POST['staffno']
			email = request.POST['email']
			area = request.POST['area']
			phoneno = request.POST['phoneno']
			idno = request.POST['idno']
			krapin = request.POST['krapin']
			commencementdate = request.POST['commencementdate']
			expirydate = request.POST['expirydate']
			sumassured = request.POST['sumassured']

			messages.success(request, ('There was an error in your input or the vehicle record already exists. Please try again.'))
			#return redirect('join')
			return render(request, 'join.html', {'regno':regno,
				'firstname':firstname,
				'middlename':middlename,
				'lastname':lastname,
				'staffno':staffno,
				'email':email,
				'area':area,
				'phoneno':phoneno,
				'idno':idno,
				'krapin':krapin,
				'commencementdate':commencementdate,
				'expirydate':expirydate,
				'sumassured':sumassured,
				})
	else:
		return render(request, 'join.html', {})