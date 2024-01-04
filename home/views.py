from django.shortcuts import render
import shopify
from shopify_app.decorators import shop_login_required

@shop_login_required
def index(request):
    # products = shopify.Product.find(limit=3)
    # orders = shopify.Order.find(limit=3, order="created_at DESC")
    context = {
        'products': 'products', 
        'orders': 'orders'
    }

    response = render(request, 'home/index.html', context)
    
    # Add headers to allow framing
    response['X-Frame-Options'] = 'ALLOWALL'
    response['Content-Security-Policy'] = "frame-ancestors 'self' *"
    
    return response
