from django import forms
from .models import Topic,Comments

class CommentForm(forms.ModelForm):
	class Meta:
		model= Comments
		fields = ['userComment','comments','topc_title']
