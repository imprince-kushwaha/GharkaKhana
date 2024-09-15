from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from myApp.models import Food_Section,Address,Contact,Payment,Order
import json
# Create your views here.
from Ghar_ka_khana.settings import *
from time import time
import razorpay 
client=razorpay.Client(auth=(KEY_ID,KEY_SECRET))

from django.views.decorators.csrf import csrf_exempt


def home(request):
    food_show=Food_Section.objects.all()
    data={
        'food_show':food_show,
    }
    return render(request,'index.html',data)


def handleSignup(request):
    if request.method=='POST':
        Name=request.POST.get('signupusername')
        Email=request.POST.get('signupemail')
        Password=request.POST.get('signuppassword')
        Password2=request.POST.get('signuppassword2')

        if Password!=Password2:
            return HttpResponse("<center><h2>Your Password and Confirm Password is not correct!!</h2></center>")
        else:
            my_user=User.objects.create_user(Name,Email,Password)
            my_user.save()
            return redirect('signin')
    return render(request,'signup.html')
    

def handleSignin(request):
    if request.method=='POST':
        Username=request.POST.get('loginname')
        Userpassword=request.POST.get('loginpassword')
        user=authenticate(request,username=Username,password=Userpassword)
        # print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is Incorrect ")
    return render(request,'signin.html')

def logOut(request):
    logout(request)
    return redirect('home')

def contact1(request):
    if request.method=='POST':
        Con_name=request.POST.get('name')
        Con_email=request.POST.get('email')
        Con_mob=request.POST.get('mobile')
        Con_desc=request.POST.get('desc')
        print(Con_desc)
        contact_details=Contact(user_name=Con_name,user_email=Con_email,user_mob=Con_mob,user_desc=Con_desc)
        contact_details.save()
        return redirect('home')
    return render(request,'index.html')



def food_donation(request):
    return render(request,'food_donation.html')

def order(request):
    if request.user.is_staff:
        my_order=Order.objects.all()
    else:
        my_order=Order.objects.filter(user=request.user)
        # Food_Section

    data={
        'my_order':my_order,
    }
    return render(request,'myorder.html',data)


def checkout(request):
    if request.method=='POST':
        address=request.POST.get("addr")
        e_mail=request.POST.get("email")
        mob=request.POST.get("num")
        pcode=request.POST.get("pin_code")
        sum=request.POST.get("amount")
        cart=request.POST['cart_data']
        print("hello")
        print(cart)
        print("heo")
        try:
           cart=json.loads(cart)
        except json.JSONDecodeError as e:
            print("JSON decoding error:", e)


        user=request.user
        order=None
        amount=int(sum)*100
        currency="INR"
        notes={
            'email':'kushwaha@gmail.com',
            'name':'pk',
        }
        
        receipt=f"Ghar Ka Khana--{int(time())}"
        order=client.order.create({'receipt':receipt,'currency':currency,'notes':notes,'amount':amount})
        payment=Payment.objects.create(user=user,order_id=order.get('id'),amount=int(sum))

       
        for i in cart:
            orderitem=Order.objects.create(user=user,food_name=i['title'],count=i['quantity'])
            payment.ordered_items.add(orderitem)
            print(payment)
        

        dict1={
            'order':order,
            'user':user,
        }
        # user=request.user,
        deliv_add=Address(address=address,email=e_mail,mob=mob,pin=pcode,amount=amount,order_id=order['id'])
        deliv_add.save()
        return render(request,'cartshow.html',dict1)
    return render(request,'cartshow.html')
 
def menu(request):
    return render(request,'menu.html')

@csrf_exempt
def success(request):
    if request.method=='POST':
        # data = json.loads(request.body)
        data=request.POST
        client.utility.verify_payment_signature(data)
        razorpay_order_id=data['razorpay_order_id']
        razorpay_payment_id = data['razorpay_payment_id']
        payment=Payment.objects.get(order_id=razorpay_order_id)
        payment.payment_id=razorpay_payment_id
        payment.status=True
        print(razorpay_order_id)
        print(razorpay_payment_id)
        if Payment.objects.filter(payment_id=razorpay_payment_id).exists():
            pass
        else:
            payment.save()
        return render(request,'success.html')
        
    return  render(request,'success.html')