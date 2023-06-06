from django.shortcuts import render,HttpResponse,redirect
from products.models import Product
from accounts.models import Cart
from base.helpers import save_pdf
from django.contrib import messages
# Create your views here.

def index(request):

    context =  {'products': Product.objects.all()}
    return render(request, 'home/index.html',context)

def delivery(request):
    cart_obj = Cart.objects.get(is_paid=False, user=request.user)
    print(cart_obj.cart_items)
    if cart_obj.cart_items.exists():
        cart_obj = Cart.objects.get(is_paid=False, user=request.user)
        pdf_file_name, pdf_saved = save_pdf({'cart':cart_obj},user=request.user)
        if pdf_saved:
            # PDF saved successfully, do further processing or redirect as needed
            # For example, you can pass the generated PDF file name to the delivery.html template
            cart_obj.delete()
            cart_obj.save()
            return render(request, 'product/delivery.html', {'pdf_file_name': pdf_file_name})
        else:
            # Error occurred while generating or saving the PDF
            # Handle the error or redirect to an error page
            return HttpResponse("Error occurred while generating PDF")
    else:
        messages.warning(request,'Your Cart is empty')
        return redirect('cart')