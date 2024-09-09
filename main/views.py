from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Rok Jeans',
        'price': 'Rp 70.000',
        'description': 'Available'
    }

    return render(request, "main.html", context)