from django.shortcuts import render
from datetime import datetime
from .models import *
# Create your views here.
def index(request):
	product=Product.objects.all()
	context={'product':product}
	return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		phone=request.POST.get('phone')
		comment=request.POST.get('comment')
		contact=Contact(name=name,email=email,phone=phone,comment=comment,date=datetime.today())
		contact.save()
	return render(request,'contact.html')