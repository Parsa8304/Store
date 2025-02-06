#Importing models and forms
from django.shortcuts import render , redirect , get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages





# homepage
#-------------------------------------------------------
def products(request):
    sort_by = request.GET.get('sort','name' )
    query = request.GET.get('q')
    if query:     # searching functionality
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all().order_by(sort_by)#calling the models
    context = {'products': products} #Database tables
    return render(request, 'ManageSys/products.html', context)



#-----------------------------------------------------------

#CRUD OPERATIONS:

#CRUD-> Create: adding new products to the website
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for image uploads
        if form.is_valid():
            product = form.save()  # Save the form and get the product instance
            messages.success(request, 'Product created successfully!')
            return redirect('products')  # Replace with your success URL
    else:
        form = ProductForm()  # Initialize the form for GET requests
    context = {'form': form}
    return render(request, 'ManageSys/new-product.html', context)


#CRUD-> Read:showing the details of the Product
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'ManageSys/product-details.html', context)


#CRUD -> Update : editing the product
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    form = ProductForm(request.POST or None, instance=product)  # Correctly initialize the form with the product instance

    if request.method == 'POST':
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated product
            return redirect('products')  # Redirect to the products list

    context = {'product': product, 'form': form}  # Prepare context for rendering
    return render(request, 'ManageSys/edit-product.html', context)  # Render the template


#CRUD -> Delete : removing the product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
       product.delete()
       messages.success(request, 'Product deleted successfully!')
       return redirect('products')
    context = {'product': product}
    return render(request, 'ManageSys/delete-product.html',context)




