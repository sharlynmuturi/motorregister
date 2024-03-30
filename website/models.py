from django.db import models

# Create your models here.
class motordetail(models.Model):
	regno = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	middlename = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	staffno = models.IntegerField()
	email = models.EmailField(default='example@example.com')
	area = models.CharField(max_length=100)
	phoneno = models.IntegerField()
	idno = models.IntegerField()
	krapin = models.CharField(max_length=100)
	commencementdate = models.DateField()
	expirydate = models.DateField()
	sumassured = models.IntegerField()

	def __str__(self):
		return self.regno

