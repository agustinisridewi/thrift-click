from django.shortcuts import render

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

    context = {
        'items': items,
        'nama': 'Agus Tini Sridewi',
        'npm': '2306276004',
        'kelas': 'PBP C',
    }

    return render(request, 'main.html', context)