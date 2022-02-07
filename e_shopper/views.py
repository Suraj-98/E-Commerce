import razorpay
from django.contrib.auth.forms import PasswordChangeForm
from django.core import paginator
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from django.views import View
from .models import *
from .forms import  *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from cart.cart import Cart
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404



# Create your views here.
def indexpage(request):
    return render(request,"index.html")

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def homepage(request):
    cat=Category.objects.all()
    brd=Brand.objects.all()
    catid=request.GET.get("category")
    brdid=request.GET.get("brand")
    if catid:
        pro=Product.objects.filter(sub_category=catid)
    elif brdid:
        pro=Product.objects.filter(brand=brdid)
    else:
        pro=Product.objects.all().order_by('date_created') 
    paginator=Paginator(pro,9)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request,"home.html",{'page_obj':page_obj,'cat':cat,'brd':brd})

def signuppage(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
    'create account',
    'successfully created your account',
    settings.EMAIL_HOST_USER,
    ['surajsharma3050@gmail.com'],
    fail_silently=False
)
            return redirect("/e_shopper/signinpage/")
 
    form = NewUserForm()    
    obj=User.objects.all()
    return render(request,"signup.html",{'form':form})
    
    
def signinpage(request):

    if request.method=='POST':
        form=CustomAuthenticationForm(request=request,data=request.POST)
        if form. is_valid():
            uname=form.cleaned_data["username"]
            pname=form.cleaned_data["password"]
            user=authenticate(username=uname,password=pname)
            if user is not None:
                login(request,user)
                request.session["msg"]="successful login"
                request.session["login"]=uname
                messages.success(request,"Signin successfully")
                return redirect("/e_shopper/homepage/")
                

    else:
        form=CustomAuthenticationForm()
    return render(request,"signinpage.html",{'form':form})


def signoutpage(request):
    del request.session["msg"]
    del request.session["login"]
    return redirect("http://localhost:8000/e_shopper/signinpage")

@csrf_exempt
@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def profilepage(request):
    pf=UpdateProfileImage.objects.filter(user=request.user)
    return render(request,"profile.html",{'pf':pf})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def updateprofile(request):
    if request.method == 'POST':
        form1=UpdateProfileImageForm(request.POST,request.FILES,instance=request.user)
        form =UserDetailsForm(request.POST,instance=request.user)
        if form1.is_valid() and form.is_valid():
            form1.save()
            form.save()
    
            
            return redirect("http://localhost:8000/e_shopper/profilepage")
    form1=UpdateProfileImageForm(instance=request.user)
    form=UserDetailsForm(instance=request.user)
    return render(request,"updateprofile.html",{'form1':form1,'form':form})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def changepassword(request):
    if request.method == "POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect("/e_shopper/signinpage")
    form=PasswordChangeForm(user=request.user)
    return render(request,"blog.html",{'form':form})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def delete(request,id):
    pi=Product.objects.filter(pk=id)
    pi.delete()
    return redirect("/e_shopper/homepage")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/e_shopper/homepage")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def cart_detail(request):
    return render(request, 'cart_details.html')

def search(request):
    query=request.GET['query']
    pro=Product.objects.filter(name__icontains=query)
    return render(request,"search.html",{'pro':pro})
    
@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def products(request):
    cat=Category.objects.all()
    brd=Brand.objects.all()
    catid=request.GET.get("category")
    brdid=request.GET.get("brand")
    if catid:
        pro=Product.objects.filter(sub_category=catid)
    elif brdid:
        pro=Product.objects.filter(brand=brdid)
    else:
        pro=Product.objects.all().order_by('date_created') 
    paginator=Paginator(pro,9)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request,"products.html",{'page_obj':page_obj,'cat':cat,'brd':brd})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def product_details(request,id):
    pro=Product.objects.filter(id=id)
    return render(request,"product_details.html",{'pro':pro})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def place_order(request):
    return render(request,"checkout.html")

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def checkout(request):
    if request.method == "POST":
        cart=request.session.get("cart")
        user=request.user
        address=request.POST.get("address")
        state=request.POST.get("state")
        mobile_no=request.POST.get("mobile_no")
        zipcode=request.POST.get("zipcode")

        for i in cart:
            a=int(cart [i] ["price"])
            b=cart [i] ["quantity"]
            total=a*b
            order=Order(
                user=user,
                product=cart [i] ['name'],
                price=cart [i] ['price'],
                quantity=cart [i] ['quantity'],
                image= cart [i] ['image'],
                address=address,
                state=state,
                mobile_no=mobile_no,
                zipcode=zipcode,
                total=total
            )
            print(order)
            order.save()
        request.session['cart']={}
        return redirect("/e_shopper/payment/")

    if request.method == "POST":
        form=CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/e_shopper/payment/")

    
    form=CheckoutForm(instance=request.user)
    return render(request,"checkout.html",{"form":form})

client = razorpay.Client(auth=("rzp_test_ppCwfU5VtNHW0Y", "6sGsvEcPdkIwSJSk5imosfUi"))
@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def payment(request):
    DATA = {
    "amount":50000,
    "currency": "INR",
    "payment_capture":"1"}
    payment=client.order.create(data=DATA)
    payment_id=payment["id"]
    return render(request,"payment.html",{"api_key":"rzp_test_ppCwfU5VtNHW0Y","id":payment_id})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def contactus(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/e_shopper/homepage/")
    form=ContactForm()
    return render(request,"contact-us.html",{"form":form})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def aboutus(request):
    return render(request,"about-us.html")

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def orderlist(request):
    order=Order.objects.filter(user=request.user)
    return render(request,"order.html",{'order':order})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def wishlist(request):
    user=request.user
    print(user)
    wish=Wishlist.objects.filter(user=request.user)
    return render(request,"wishlist.html",{'wish':wish})

@login_required(login_url="http://localhost:8000/e_shopper/signinpage")
def order_detail(request,id):
    order=Order.objects.filter(user=request.user,pk=id)
    return render(request,"order_detail.html",{'order':order})