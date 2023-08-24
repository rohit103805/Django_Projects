from asyncio.windows_events import NULL
from math import prod
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Clothes, FootWear, SkinCare, Order
from django.views.decorators.csrf import csrf_exempt
import razorpay

# Create your views here.

client=razorpay.Client(auth=('rzp_test_GzXPGVYxao14ck', 'aP4KEAy0Iuys08z8hp75NzYt'))

def login_user(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        next_page=request.POST['next']
        user = authenticate(request, username=username, password=password)
        if user:
            if(len(next_page)==0):
                next_page='/'
            login(request, user)
            return HttpResponseRedirect(next_page)
        else:
            if(len(next_page)==0):
                next_page='login'
            return HttpResponseRedirect(next_page)
    except:
        return render(request, 'Login.html')


def register(request):
    try:
        username=request.POST['Username']
        password=request.POST['Password']
        email=request.POST['Email']
        next_page=request.POST['next']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(next_page)
    except:
        next = request.GET['next']
        return render(request, 'Register.html', {'next':next})


@login_required(login_url='/login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
    return render(request, 'Home.html', {'user': user})

@login_required(login_url='/login')
def clothing(request):
    if request.user.is_authenticated:
        user=request.user
    clothes=Clothes.objects.all()
    for cloth in clothes:
        cloth.desc=cloth.desc[:20]+"...More"
    return render(request, 'Clothing.html', {'user':user, 'products':clothes})

@login_required(login_url='/login')
def footwear(request):
    if request.user.is_authenticated:
        user=request.user
    footwear=FootWear.objects.all()
    return render(request, 'FootWear.html', {'user':user, 'products':footwear})

@login_required(login_url='/login')
def skincare(request):
    if request.user.is_authenticated:
        user=request.user
    skin=SkinCare.objects.all()
    return render(request, 'SkinCare.html', {'user':user, 'products':skin})

@login_required(login_url='/login')
def product_view(request):
    id=request.GET['details']
    if(id[0]=='C'):
        id=id[1:]
        section="Clothing"
        sec="C"
        prod=Clothes.objects.get(id=id)
    elif(id[0]=='F'):
        id=id[1:]
        section="FootWear"
        sec="F"
        prod=FootWear.objects.get(id=id)
    elif(id[0]=='S'):
        id=id[1:]
        section="SkinCare"
        sec="S"
        prod=SkinCare.objects.get(id=id)
    return render(request, 'View.html', {'product':prod, 'section':section, 'sec':sec})

@login_required(login_url='/login')
def payment_page(request):
    if request.method=='POST':
        try:
            image=request.POST['image']
            name=str(request.POST['prod_name'])
            id=str(request.POST['prod_id'])
            price=int(request.POST['price'])
            address=str(request.POST['address'])
            order_date=str(DateTime())
            order_id=str(request.user)+str(order_date)
            print(order_date)
            DATA={
                "amount":price*100,
                "currency":"INR",
                "receipt": order_id,
                "payment_capture": '0',
            }
            razorpay_order = client.order.create(data=DATA)
            ord=Order.objects.create(name=name, user=str(request.user), prod_id=id, price=price, delivery_address=address, razorpay_order_id=razorpay_order['id'], razorpay_payment_id=str(NULL), razorpay_signature=str(NULL))
            ord.save()
            print(razorpay_order['id'])
            return render(request, 'Waiting.html', {'id':razorpay_order['id'], 'user':request.user, 'price':price*100, 'image':image, 'prod_name': name, 'delivery': address, 'price_disp':price})
        except:
            razorpay_id = request.POST['razorpay_id']
            print(razorpay_id)
            ord=Order.objects.get(razorpay_order_id=razorpay_id)
            prod_id = ord.prod_id
            if(prod_id[0]=='C'):
                products=Clothes.objects.get(id=prod_id[1:])
            elif(prod_id[0]=='S'):
                products=SkinCare.objects.get(id=prod_id[1:])
            elif(prod_id[0]=='F'):
                products=FootWear.objects.get(id=prod_id[1:])
            return render(request, 'Waiting.html', {'id':razorpay_id, 'user':request.user, 'price':ord.price*100, 'image':products.image.url, 'prod_name':products.name, 'delivery':ord.delivery_address, 'price_disp':ord.price})


@csrf_exempt
def success(request):
    try:
        payment_id=request.POST.get('razorpay_payment_id', '')
        order_id=request.POST.get('razorpay_order_id', '')
        signature=request.POST.get('razorpay_signature', '')
        Order.objects.filter(razorpay_order_id=order_id).update(razorpay_payment_id=str(payment_id), razorpay_signature=str(signature))
        params_dict={
            'razorpay_order_id':order_id,
            'razorpay_payment_id':payment_id,
            'razorpay_signature':signature,
        }
        result=client.utility.verify_payment_signature(params_dict)
        print(result)
        if result:
            ord=Order.objects.get(razorpay_order_id=order_id)
            price=ord.price
            try:
                client.payment.capture(payment_id, price*100)
                print("Holo order place")
                return render(request, 'Success.html')
            except:
                print("Holo na")
                Order.objects.filter(razorpay_order_id=order_id).update(razorpay_payment_id=str(0), razorpay_signature=str(0))
                return render(request, 'Failure.html')
        else:
            Order.objects.filter(razorpay_order_id=order_id).update(razorpay_payment_id=str(0), razorpay_signature=str(0))
            print("Hochhe nah")
            return render(request, 'Failure.html')
    except:
        return HttpResponse('Error 505 not found')
        
@login_required(login_url='/login')
def orders_view(request):
    orders_tab=Order.objects.filter(user=str(request.user)).all()
    return render(request, 'Orders.html', {'orders_tab': orders_tab})

@login_required(login_url='/login')
def pending_payments(request):
    pending_tab=Order.objects.filter(user=str(request.user), razorpay_payment_id=0, razorpay_signature=0).all()
    return render(request, 'Pending_Payments.html', {'pending_tab': pending_tab})

def delete(request):
    razorpay_id = request.POST['razorpay_id']
    ord=Order.objects.get(razorpay_order_id=razorpay_id)
    ord.delete()
    return HttpResponseRedirect('/pending_payments')