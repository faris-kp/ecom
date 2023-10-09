from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from userauths.models import User
# from django.conf import settings

# # Create your views here.

# User = settings.AUTH_USER_MODEL  # same as the effect - from userauths.models import User  instead of i am using User  import


def register_view(request):
    
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Hey { username }, your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
                    )
            login(request,new_user)
            return redirect("index")
    else:
        form = UserRegisterForm()
            
    context ={
        
            'form':form
        }
    return render(request,'userauths/sign-up.html',context)


def login_view(request):
    
    if request.user.is_authenticated:
        messages.warning(request, f"Hey You are already logged in")
        return redirect("index")
    
    if request.method == "POST":
        print("user cheking in login ",request.user)
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("email cheking",email)
        print("password",password)
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email ,password=password)
        
            if user is not None:
                login(request,user)
                messages.success(request, f"You logged in succesfully")
                return redirect("index")
        except:
            messages.warning(request, f"User with this { email } does not exist")
            
    return render(request,"userauths/sign-in.html")
            
def logout_view(request):
    print("Entered into logout view")
    
    logout(request)
    messages.success(request, f"You are logged out ")
    return redirect("userauths:sign-in")