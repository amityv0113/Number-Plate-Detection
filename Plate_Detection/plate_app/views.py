
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse



from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

from plate_app.login_form import UserForm,UserProfileInfoForm


# Create your views here.

def home_page(request):
    return render(request, 'basic_html/introduction.html')


def introduction_page(request):
    return render(request,'basic_html/base.html')

def algorithm_page(request):
    return render(request,'basic_html/algorithm.html')


def machine_learing(request):
    return render(request,'basic_html/machine_learing.html')

def more_page(request):
    return render(request,'basic_html/more.html')


def register(request):
    
    registered = False
    
    if request.method == "POST":
        
        user_form = UserForm(data = request.POST)
        
        #profile_form =UserProfileInfoForm(data = request.POST)
        
        if user_form.is_valid(): #and profile_form.is_valid():
            
            user =user_form.save()
            user.set_password(user.password) #convert normal password into hash 
            user.save()
            
            #profile = profile_form.save(commit =False)
            
            profile.user =user
            
            #if 'profile_pic' in request.FILES:
                
                #profile.profile_pic =request.FILES['profile_pic']
                
            #profile.save()
            
            registered =True  
            
        #else:
            
           # print(user_form.errors,profile_form.errors) 
            
    else:
        
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    
    return render(request,'basic_html/registration.html',{'user_form':user_form ,'registered':registered}) #'profile_form':profile_form,
        
@login_required              
def special(request):
    return HttpResponse("You are Login")
             
                
@login_required           
def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))
                  
def index1(request):
    return render(request,'basic_html/login.html')           
            


def user_login(request):
    
    if request.method =='POST':
        
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home_page'))
                
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
            
        else:
            print('some one tried to login and fail')
            return HttpResponse("invalid login detail supplied")
        
    else:
        
        return render(request,'basic_html/login.html')
                

