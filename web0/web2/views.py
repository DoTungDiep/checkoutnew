from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem
from django.http import HttpResponse
def signup(request):
    if request.method == 'POST':
        u_name_signup= request.POST.get('user_namesu')
        pw_signup= request.POST.get('passwordsu')
        #store users
        users = request.session.get('users', {})
        users[u_name_signup] = pw_signup
        request.session['users'] = users
        return redirect("login")
    return render(request, "signup.html")

def login(request):
    if request.method == 'POST':
        u_name = request.POST.get('user_name')
        pw = request.POST.get('password')
        users = request.session.get('users', {})
        if u_name in users and users[u_name] == pw:
            redirect('list')
    return render(request, "login.html")
    


# Dummy cart items for demo (replace with your cart system)
def checkout(request):
    food = request.GET.get('food',)
    price = int(request.GET.get('price',))
    quantity = int(request.GET.get('quantity',))
    food1 = request.GET.get('food1')
    price1 = int(request.GET.get('price1',))
    quantity1 = int(request.GET.get('quantity1',))
    total = (price * quantity)+(price1 * quantity1) 
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect("confirm")
        else:
            print("INVALID")
            print(form.errors)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {
        'food': food,
        'price': price,
        'quantity': quantity,
        'total': total,
        'form': form,
        'food1':food1,
        'price1': price1,
        'quantity1':quantity1
    })
def success(request):
    return render(request, "success.html")

def confirm(request):
    return render(request,"cf.html")

def list(request):
    return render(request, "list.html")
def home(request):
    return render(request, 'home.html')