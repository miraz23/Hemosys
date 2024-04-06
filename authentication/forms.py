from django import forms
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import userprofile
from .models import bloodbank

class signupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name  = forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields  = ('email', 'first_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        

        if commit:
            user.save()
        return user
     

class userprofileForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ('phone', 'location', 'bloodgroup', 'age', 'gender', 'image')

class bloodbankForm(forms.ModelForm):
    class Meta:
        model = bloodbank
        fields = ('bloodbankname', 'bloodbankemail', 'bloodbankphone', 'bloodbanklink', 'bloodbanklocation', 'bloodbanktypes', 'bloodbankgroups', 'bloodbankaccreditations', 'image')


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = userprofile
        fields = ('phone', 'location', 'bloodgroup', 'age', 'gender', 'image')