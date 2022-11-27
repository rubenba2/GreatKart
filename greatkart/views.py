from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True) #Status true to show the reviews. If you set the reviews as false, those won't show in the site.


    context = {
        'products': products,
        'reviews':reviews,
    }

    return render(request, 'home.html', context)