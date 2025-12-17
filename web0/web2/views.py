from django.shortcuts import render

def ho(request):
    return render(request, "ho.html")

from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem


# Dummy cart items for demo (replace with your cart system)
def checkout(request): 
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect("confirm")
        else:
            print("INVALID")
            print(form.errors)
    else:
        form = CheckoutForm()
        return render(request,'checkout.html',{
            'form':form,
        })
def success(request):
    return render(request, "success.html")

def confirm(request):
    quantity = int(request.session.get('quantity',0))
    food1 = request.session.get('food1')
    price1 = int(request.session.get('price1'))
    quantity1 = int(request.session.get('quantity1',0))
    food = request.session.get('food')
    price = request.session.get('price')
    total = (price * quantity)+(price1 * quantity1)
    return render(request,"cf.html",{
        'food': food,
        'price': price,
        'quantity': quantity,
        'total': total,
        'food1':food1,
        'price1': price1,
        'quantity1':quantity1
    })

def list(request):
    request.session['food'] = request.GET.get('food')
    request.session['price'] = request.GET.get('price')
    request.session['quantity1'] = request.GET.get('quantity1')
    request.session['quantity'] = request.GET.get('quantity')
    request.session['price1'] = request.GET.get('price1')
    request.session['food1'] = request.GET.get('food1')
    return render(request, "list.html")