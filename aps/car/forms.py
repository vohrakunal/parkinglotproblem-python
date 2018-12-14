from django import forms
from car.models import car

class NewCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ('regno', 'color')

class RemoveCarForm(forms.ModelForm):
    class Meta:
        model = car
        fields =('regno',)

class SearchCarForm(forms.Form):
          searchfield = forms.CharField(max_length=100)

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = adminlogin
#         fieds = ('username', 'password')
