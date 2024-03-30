from django import forms
from django.core.exceptions import ValidationError
from .models import motordetail

class motordetailForm(forms.ModelForm):
	class Meta:
		model = motordetail
		fields = ['regno', 'firstname', 'middlename', 'lastname', 'staffno', 'email', 'area', 'phoneno', 'idno', 'krapin', 'commencementdate', 'expirydate', 'sumassured']

	def clean_regno(self):
		regno_value = self.cleaned_data.get('regno')

		#check if a record with the same entryfor regno already exists
		if motordetail.objects.filter(regno=regno_value).exists():
			raise ValidationError("A record with this entry already exists.")

		return regno_value