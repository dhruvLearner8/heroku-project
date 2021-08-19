from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Comp_detail, Desc
import smtplib
import random
import email.message

# Create your views here.
def home(request):
    return render(request,'main_page_sgp.html')


def explore(request):
    return render(request,"explore.html")

def index(request):
    if 'comp_user' in request.session.keys():
        User=Comp_detail.objects.get(id=int(request.session['comp_user']))
        descM=Desc.objects.filter(user1=User)
        return render(request,"index.html",{'USER':User,'DESC': descM})      
    else:
        return redirect('login')

def add(request):
    if 'comp_user' in request.session.keys():
        User=Comp_detail.objects.get(id=int(request.session['comp_user']))
        if request.method=='POST':
            descM=Desc()
            desc1=request.POST['desc']
            
            amt=float(request.POST.get('amount'))
            
            op1=User.income
            op2=User.expense
            type1=request.POST.get('choice')
            if type1=='add':
                op1=op1+float(amt)
                
            elif type1 =='sub':
                op2=op2+float(amt)
            User.income=op1
            User.expense=op2
            User.balance=op1-op2
            User.save()
            descM.user1=User
            descM.amount=amt
            descM.desc=desc1
            descM.type1=type1
            descM.save()
        return redirect('index')
    else:
        return redirect('login')




def register(request):
    if request.method=='POST':
        un=request.POST['username']
        em=request.POST['email']  
        p1=request.POST['password']
        p2=request.POST['password_confirm'] 

        try:
            obj=Comp_detail.objects.get(email=em)
            return HttpResponse('email already taken')
        except:
            if p1==p2:
                obj=Comp_detail()
                obj.username=un
                obj.email=em
                obj.password=p1
                obj.save()
                return redirect('login')
            else:
                return HttpResponse('wrong password')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        em=request.POST['email']
        p1=request.POST['password']
        try:
            obj=Comp_detail.objects.get(email=em)
            if p1==obj.password:
                request.session['comp_user']=obj.id
                return redirect('index')
            else:
                return HttpResponse('wrong password entered')
        except:
            return HttpResponse('wrong email address entered')
    return render(request,'login.html')

def logout(request):
    if 'comp_user' in request.session.keys():
        del request.session['comp_user']
        return redirect('login')
    else:
        return redirect('login')



def forget_pass(request):
    if request.method=='POST':
        em=request.POST['email']
        print(em)
        try:
            obj=Comp_detail.objects.get(email=em)
            sender_email='dhruvwork416@gmail.com'
            sender_pass='Dhruv2001'
            recieve_email=em
            server=smtplib.SMTP('smtp.gmail.com',587)

            # OTP CREATE-------------
            no=[1,2,3,4,5,6,7,8,9,0]
            otp=""
            for i in range(6):
                otp+=str(random.choice(no))
            print(otp)

            mess1= f"""
            This Is Your OTP
            {otp}

            Dont share with Others

            """
            msg=email.message.Message()
            msg['Subject']="OTP from Dinero"
            msg['From'] = sender_email
            msg['To']= recieve_email
            password = sender_pass
            msg.add_header('Content-Type','text/html')
            msg.set_payload(mess1)

            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'],msg['To'],msg.as_string())
            request.session['otp']=otp
            request.session['USERS'] = obj.id
            return redirect('OTP_check')

        except:
            return HttpResponse('wrong email address entered')
        
    return render(request,'forget_pass.html')

def OTP_check(request):
    if 'otp' in request.session.keys():
        if request.method=='POST':
            ot1=request.POST['otp']
            if ot1==request.session['otp']:
                del request.session['otp']
                return redirect('new_pass')
            else:
                del request.session['otp']
                return redirect('forget_pass')
        return render(request,'OTPcheck.html')
    else:
        return render('login')

def new_pass(request):
    if 'USERS' in request.session.keys():
        return render(request,'new_pass.html')
    else:
        return redirect('login')


def Delete_Product(request,id):
    if 'comp_user' in request.session.keys():  
        prod = Desc.objects.get(id = id)
        prod.delete()
        return redirect('index')
    else:
        return redirect('login')

def history(request):
    if 'comp_user' in request.session.keys():
        User=Comp_detail.objects.get(id=int(request.session['comp_user']))
        descM=Desc.objects.filter(user1=User)
        return render(request,"history.html",{'USER':User,'DESC': descM})      
    else:
        return redirect('login')


def new_pass(request):
    if 'USERS' in request.session.keys():
        if request.POST:
            p1 = request.POST['pas1']
            p2 = request.POST['pas2']
            
            if p1 == p2:
                obj = Comp_detail.objects.get(id = int(request.session['USERS']))
                obj.password = p2
                obj.save()
                del request.session['USERS']
                return redirect('login')
            else:
                return HttpResponse('<a href=""> Both Passwords are Not Same... </a>')
            
        return render(request,'new_pass.html')
    else:
        return redirect('login')