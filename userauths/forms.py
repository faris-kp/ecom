from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username",
                "style": "height: 40px; width: 300px; border-radius: 10px; border: 2px solid #ccc;",                                       
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email",
            "style": "height: 40px; width: 300px; border-radius: 10px; border: 2px solid #ccc;",                                               
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password1",
                "style": "height: 40px; width: 300px; border-radius: 10px; border: 2px solid #ccc;",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password2",
                "style": "height: 40px; width: 300px; border-radius: 10px; border: 2px solid #ccc;",      
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email']