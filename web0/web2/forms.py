from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    print("ty")

    class Meta:
        model = Order
        fields = ["full_name", "email", "address", "city", "love"]