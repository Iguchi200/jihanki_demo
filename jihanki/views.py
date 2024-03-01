from django.shortcuts import render, get_object_or_404

from jihanki.models import Product

def product_list(request):
  products = Product.objects.all()
  return render(request, "jihanki/product_list.html", {"products": products})

def buy_product(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if product.stock > 0:
    product.stock -= 1
    product.save()
  return render(request, "jihanki/buy_product.html", {"product": product})
