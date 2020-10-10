from django import forms
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from  .models import Profile
# from .models import
User = get_user_model()
 
class SignUpForm(UserCreationForm):
    class  Meta:
        model = User
        fields = ['username','email','password1','password1','first_name','last_name','email']



class UserForm(UserCreationForm):

    class  Meta:
        model = User
        fields = ['username','email','password1','password1']



class ProfileEditForm(forms.ModelForm):

    class  Meta:
        model = Profile
        fields = ['image','phon_number','bio','haedline']
        
class UserEditForm(forms.ModelForm):
    
    class  Meta:
        model = User
        fields = ['username','first_name','last_name','email',]