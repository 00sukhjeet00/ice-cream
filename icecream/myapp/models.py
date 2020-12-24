from django.db import models

class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=12)
	comment=models.TextField()
	date=models.DateField()
	def __str__(self):
		return self.name
class Product(models.Model):
	name=models.CharField(max_length=200)
	desc=models.TextField()
	date=models.DateField()
	img=models.ImageField(upload_to='static/')
	def __str__(self):
		return self.name