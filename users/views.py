# views.py in your new app
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from shop.models import Product
from .forms import ProductForm,LoginForm,ProductUpdateForm
from order.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('users:vendor')  # Redirect to the dashboard or any other desired URL after login
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def display_products(request):
    orders = Order.objects.all()
    count_orders = orders.count()
    products = Product.objects.all()
    context={
        'products': products,
        'count':count_orders

    }
    return render(request, 'users/interface.html', context)


def add_product(request):
    orders = Order.objects.all()
    count_orders = orders.count()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:vendor')  # Redirect to the product list page
    else:
        form = ProductForm()

    return render(request, 'users/add.html', {'form': form, 'count':count_orders,})


def display_orders(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order = Order.objects.get(id=order_id)
            order.delivered = True
            order.save()
            return redirect('users:orders')

    orders = Order.objects.all()
    count_orders = orders.count()
    
    return render(request, 'users/orders.html', {'orders': orders, 'count': count_orders})


@login_required
def user_profile(request):
    orders = Order.objects.all()
    count_orders = orders.count()
    products = Product.objects.all()
    products_count = products.count()
    
    user = request.user
    context = {'user': user , 'count':count_orders,'prodcount':products_count}
    return render(request, 'users/profile.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect(reverse('shop:Home')) # Redirect to the home page or any other desired URL after logout


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        p_form = ProductUpdateForm(request.POST, instance=product)
        if p_form.is_valid():
            p_form.save()
            print("Changes saved.")
            return redirect('users:edit-product', product_id=product.id)

    else:
        p_form = ProductUpdateForm(instance=product)

    context = {
        'p_form': p_form,
        'product': product,
    }

    return render(request, 'users/editproduct.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        # Redirect to the product list or any other desired page
        return redirect('users:vendor')

    # If the request method is not POST, render the confirmation page
    return render(request, 'users/deleteproducts.html', {'product': product})
