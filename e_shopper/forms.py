from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user



class CustomAuthenticationForm(AuthenticationForm):
	class Meta:
		fields=("username","password")


class UserDetailsForm(forms.ModelForm):
	class Meta:
		model=User
		fields=("username", "email","first_name","last_name")


class UpdateProfileImageForm(forms.ModelForm):
	class Meta:
		model=UpdateProfileImage
		fields="__all__"

class CheckoutForm(forms.ModelForm):
	class Meta:
		model=Order
		fields=("address","state","mobile_no","zipcode")

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact
		fields="__all__"