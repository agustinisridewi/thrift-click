from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product

def show_main(request):
    items = [
        {
            'name': 'Chunky Platform Shoes',
            'price': '200000',
            'description': 'Bold, chunky platform shoes perfect for Y2K fashion lovers.',
        },
        {
            'name': 'Ripped Jeans',
            'price': '100000',
            'description': 'High-waisted distressed denim for that laid-back grunge look.',
        },
        {
            'name': 'Track Jacket',
            'price': '150000',
            'description': 'Vintage Nike track jacket with bold colors and retro design.',
        },
        {
            'name': 'Graphic Tee',
            'price': '50000',
            'description': 'Vintage band tee with iconic 90s graphics.',
        }
    ]

    product_entries = Product.objects.all()

    for product in product_entries:
        items.append({
            'name': product.name,
            'price': product.price,
            'description': product.description,
        })

    context = {
        'items': items,
        'nama': 'Agus Tini Sridewi',
        'npm': '2306276004',
        'kelas': 'PBP C',
        'product_entries': product_entries
    }

    return render(request, 'main.html', context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")