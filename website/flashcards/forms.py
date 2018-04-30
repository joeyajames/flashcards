from django import forms
from .models import Flashcard
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
	
class UploadFileForm(forms.ModelForm):
	class Meta:
		model = Flashcard
		fields = ('topic', 'keywords')
	file = forms.FileField()
	
# class UploadFileForm(forms.Form):
	# topic = forms.ModelChoiceField(queryset=Topic.objects.all())
	# file = forms.FileField()

