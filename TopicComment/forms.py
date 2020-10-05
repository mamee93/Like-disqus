from django import forms
from .models import Topic,Comments

class CommentForm(forms.ModelForm):
	class Meta:
		model= Comments
		fields = ['comments']

class ReplyForm(forms.ModelForm):
	class Meta:
		model= Comments
		fields = ['comments']

