#USER FORMS

#DJANGO

from django import forms

#MODELS
from django.contrib.auth.models import User
from users.models import Profile



class SignupForm(forms.Form):
	#SIGNUP FORM
	username = forms.CharField(min_length=4, max_length=50)

	password = forms.CharField(max_length=70, widget=forms.PasswordInput())
	password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)

	email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

	def clean_username(self):
		#USERNAME MUST BE UNIQUE
		username = self.cleaned_data['username']
		username_taken = User.objects.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError('El usuario ya existe.')
		return username

	def clean(self):
		#VERIFY PASSWORD CONFIRMATION MATCH
		data = super().clean()

		password = data['password']
		password_confirmation = data['password_confirmation']
		if password != password_confirmation:
			raise forms.ValidationError('Las contraseñas no coinciden')

		return data	

	def save(self):
		#CREATE USER AND PROFILE 
		data = self.cleaned_data
		data.pop('password_confirmation')

		user = User.objects.create_user(**data)
		profile = Profile(user=user)
		profile.save()
