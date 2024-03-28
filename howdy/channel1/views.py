import random
from django.shortcuts import render,redirect,HttpResponse
from channel1.models import UserProfile,UserOtp
from django.http import JsonResponse
from random import randint
import json



def signup(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        print("signup",data)
        mobile = data['mobile']
        try:
            exit_mob=UserProfile.objects.get(mobile=mobile)
        except:
            UserOtp.objects.create(otp=randint(0,9999),mobile=mobile)
            return redirect("/channel1/verify")
        if exit_mob==mobile:
            print(">>>>>>>>>>>>>>>>>>") 
            return JsonResponse({'status':False,'message':'Number already exist please login'})
    return render(request,"signup.html")

        
def verify(request):
    if request.method=='POST':
        data=json.loads(request.body)
        print(">>>>",data['otp'])
        # otp=
        # if otp!=data['otp']:
        #     return JsonResponse({'status':False,"message":"Invalid Otp"})
        # else:
        #     return JsonResponse({'status':'True','message':'SignUp successfully Login'})
    return render(request,"verify.html")
    
        
def login(request):
    pass

def index(request):
    return render(request,'index.html')
