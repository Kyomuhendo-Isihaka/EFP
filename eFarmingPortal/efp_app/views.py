from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from efp_app import models
import os
# Create your views here.

def efarm(request):
    return render(request, 'index.html')

def all_categories(request):
    categories=models.Category.objects.all()
    return render(request, 'all_categories.html', {'categories':categories})

def all_products(request): 
    products = models.Product.objects.all()   
    return render(request, 'all_products.html', {'products':products})

def product_details(request, pk):
    product = get_object_or_404(models.Product, productID=pk)
    context = {
        'product':product,
    }
    return render(request, 'pages/product_details.html', context)


def category_products(request, categoryID):
    products= models.Product.objects.all()
    category = get_object_or_404(models.Category, categoryID=categoryID)
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'pages/category_products.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




def dashboard(request, role, user_id):
    if role == 'admin':
        user = get_object_or_404(models.Admin, adminID=user_id)
    elif role == 'farmer':
        user = get_object_or_404(models.Farmer, farmerID=user_id )       
    elif role == 'customer':
        user = get_object_or_404(models.Customer, customerID=user_id )     
        
    context={
        'role':role,
        'user_id':user_id,
        'user':user
    }
    return render(request, 'dashboard.html', context)

def products(request, role, user_id, pk=None):
    if role == 'admin':
        user = get_object_or_404(models.Admin, adminID=user_id)
    elif role == 'farmer':
        user = get_object_or_404(models.Farmer, farmerID=user_id )       
    elif role == 'customer':
        user = get_object_or_404(models.Customer, customerID=user_id )
    
    if pk:
        product = get_object_or_404(models.Product, pk=pk)
        previous_image = product.image if product else None
    else:
        product = None
        previous_image = None

    if request.method=="POST":
        title = request.POST.get('title')
        catId = request.POST.get('product_category')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        farmerId = request.POST.get('farmerId')

        categoryId, created = models.Category.objects.get_or_create(categoryID=catId)
        farmerId, created = models.Farmer.objects.get_or_create(farmerID=farmerId)        
      

        if 'image' in request.FILES:
            new_image = request.FILES['image']
        else:
            new_image = None

        if product:
            product.title = title
            product.categoryID = categoryId
            product.description = description
            product.quantity = quantity
            product.price=price

            if new_image:
                product.image = new_image
            elif previous_image:
                product.image = previous_image

            product.save()
        else:
            product = models.Product(categoryID=categoryId, farmerID = farmerId, title=title, description=description, quantity=quantity, price=price, image=new_image)
            product.save()

            return redirect('products', role=role, user_id=user_id) 

    categories = models.Category.objects.all()
    products = models.Product.objects.all().order_by('-productID')
   
        
    context={
        'role':role,
        'user_id':user_id,
        'user':user,
        'categories':categories,
        'products':products,

    }
    return render(request, 'pages/products.html', context)

def delete_product(request, role, user_id, pk):
    product = get_object_or_404(models.Product, pk=pk)
  
    image_path = product.image.path if product.image else None

    product.delete()
    if image_path and os.path.isfile(image_path):
        os.remove(image_path)
    return redirect('products', role=role, user_id=user_id)
 

def categories(request, role, user_id, pk=None):
    if role == 'admin':
        user = get_object_or_404(models.Admin, adminID=user_id)
    elif role == 'farmer':
        user = get_object_or_404(models.Farmer, farmerID=user_id)
    elif role == 'customer':
        user = get_object_or_404(models.Customer, customerID=user_id)

    if pk:
        category = get_object_or_404(models.Category, pk=pk)
        previous_image = category.image if category else None
    else:
        category = None
        previous_image = None

    if request.method == 'POST':
               
        title = request.POST['title']
        description = request.POST['description']

        if 'image' in request.FILES:
            new_image = request.FILES['image']
        else:
            new_image = None

        if category:
            category.title = title
            category.description = description

            if new_image:
                category.image = new_image
            elif previous_image:
                category.image = previous_image

            category.save()
           
        else:
            category = models.Category(title=title, description=description, image=new_image)
            category.save()
            

        return redirect('categories', role=role, user_id=user_id) 

    categories = models.Category.objects.all()

    context = {
        'role': role,
        'user_id': user_id,
        'user': user,
        'categories': categories,
        
    }
    return render(request, 'pages/categories.html', context)



def delete_category(request, role, user_id, pk):
    category = get_object_or_404(models.Category, pk=pk)
  
    image_path = category.image.path if category.image else None

    category.delete()
    if image_path and os.path.isfile(image_path):
        os.remove(image_path)
    return redirect('categories', role=role, user_id=user_id)
    

def farmers(request, role, user_id):
    if role == 'admin':
        user = get_object_or_404(models.Admin, adminID=user_id)
    elif role == 'farmer':
        user = get_object_or_404(models.Farmer, farmerID=user_id )       
    elif role == 'customer':
        user = get_object_or_404(models.Customer, customerID=user_id )     
    
    farmers = models.Farmer.objects.all()
        
    context={
        'role':role,
        'user_id':user_id,
        'user':user,
        'farmers':farmers
    }
    return render(request, 'pages/farmers.html', context)

def customers(request, role, user_id):
    if role == 'admin':
        user = get_object_or_404(models.Admin, adminID=user_id)
    elif role == 'farmer':
        user = get_object_or_404(models.Farmer, farmerID=user_id )       
    elif role == 'customer':
        user = get_object_or_404(models.Customer, customerID=user_id )     

    customers=models.Customer.objects.all()

    context={
        'role':role,
        'user_id':user_id,
        'user':user,
        'customers':customers
    }
    return render(request, 'pages/customers.html', context)


def login(request, role):
    msg = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = None
        user_id = None

        try:
            if role == 'admin':
                user = get_object_or_404(models.Admin, username=username, password=password)
                user_id = user.adminID
            elif role == 'farmer':
                user = get_object_or_404(models.Farmer, username=username, password=password)
                user_id = user.farmerID
            elif role == 'customer':
                user = get_object_or_404(models.Customer, username=username, password=password)
                user_id = user.customerID

            return redirect('dashboard', role=role, user_id=user_id)
        except Http404:
            msg = "Wrong username or password"

    context = {
        'msg': msg,
        'role': role  
    }
    return render(request, 'login.html', context)

def logout(request):
        return redirect('efarm')

def registration(request):
    msg=''
    role=None
    user_id=None
    if request.method=="POST":
        first_name=request.POST.get('fname')
        last_name= request.POST.get('lname')
        username = request.POST.get('username')
        phone_number=request.POST.get('phone_num')
        email_address = request.POST.get('email_address')
        address=request.POST.get('address')
        user_role=request.POST.get('role')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        if password !=conf_password:
            msg="passwords didn't match"
        else:
            if user_role=='admin':
                user = models.Admin(first_name=first_name, last_name=last_name, username=username, phone_number=phone_number, email_address=email_address, role=user_role, address=address,password=password)
            elif user_role=='farmer':
                 user = models.Farmer(first_name=first_name, last_name=last_name, username=username, phone_number=phone_number, email_address=email_address, role=user_role, address=address,password=password)
            elif user_role=='customer':
                user = models.Customer(first_name=first_name, last_name=last_name, username=username, phone_number=phone_number, email_address=email_address, role=user_role, address=address,password=password)

        user.save()
        return redirect('login', role=user_role)

        
    context = {
        'role':role,
        'msg':msg      
    }
    return render(request, 'registration.html', context)