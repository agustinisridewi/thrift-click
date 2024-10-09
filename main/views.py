import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from main.forms import ProductEntryForm
from main.models import Product
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,       
        'npm': '2306276004',
        'kelas': 'PBP C',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, 'Product added successfully!')  # Success message
        return redirect('main:show_main')  # Redirect to show_main
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/json")

def show_json(request):    
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")
   
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    editproduct = Product.objects.get(pk = id)

    form = ProductEntryForm(request.POST or None, instance=editproduct)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    delproduct = Product.objects.get(pk = id)
    delproduct.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    user = request.user

    # Check for potential XSS attack
    if '<' in request.POST.get("name") or '>' in request.POST.get("name") or \
        '<' in request.POST.get("description") or '>' in request.POST.get("description"):
        messages.error(request, "This field cannot be blank")
        return HttpResponse("This field cannot be blank", status=400)

    # Buat produk baru
    new_product = Product(
        name=name,
        description=description,
        price=price,
        user=user
    )

    new_product.save()
    return redirect('main:show_main')