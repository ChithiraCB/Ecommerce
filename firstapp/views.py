
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from . models import CustomUser
from . models import CustomerProfile,Product


#from django.contrib.auth.models import User

def index(request):
    # if request.user.is_authenticated:
     return render(request, 'index.html')
 

def register_user(request):
    if request.method == "POST":
        username=request.POST.get('email')
        fullName = request.POST.get('fullName') 
        #lname = request.POST.get('lastname')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        phone = request.POST.get('phone')
        #address = request.POST.get('address')
        email = request.POST.get('email')
        

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        elif password != confirmPassword:
            messages.error(request, "Passwords do not match")
        else:
            user = CustomUser(fullName=fullName,username=username, email=email,phone=phone, user_types='2')  # Change role as needed
            user.set_password(password)
            user.save()
            messages.success
            (request, "Registered successfully")
            return redirect("login")
        # if form.is_valid():
        #     try:
        #         form.save()
        #         # Redirect to a success page or login page
        #         return redirect('login')
        #     except IntegrityError:
        #         # Handle the case where a duplicate username is entered
        #         form.add_error('username', 'This username is already taken.')
        # else:
        #     form = SignupForm()
    return render(request, "register.html")
    
def login_user(request):
    if 'username' in request.session:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # if user is not None:
        #     auth_login(request, user)
        #     return redirect('/userhome')
        # else:
        #    messages.success(request,("Invalid credentials."))
        # print(username)  # Print the email for debugging
        # print(password)  # Print the password for debugging


        if username and password:
            user = authenticate(request, username =username , password=password)

            if user is not None:
                auth_login(request,user)
                
                
            
                if request.user.user_types==CustomUser.CUSTOMER:
                    request.session["username"]=user.username
                    return redirect('userhome')
                # elif request.user.user_typ == CustomUser.VENDOR:
                #     print("user is therapist")
                #     return redirect(reverse('therapist'))
       
                
                elif request.user.user_types == CustomUser.ADMIN:
                    print("user is admin")                   
                    return redirect('adminpanel')
                # else:
                #     print("user is normal")
                #     return redirect('')

            else:
                messages.success(request,("Invalid credentials."))
                
        else:
            messages.success(request,("Please fill out all fields."))
        
    return render(request, 'login.html')

def product_grid(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product.html', {'products': products})


def adminpanel(request):
    return render(request, 'adminpanel.html')


def logout_user(request):
    # if request.user.is_authenticated:
    # if 'username' in request.session:
    #     request.session.flush()
    logout(request)
    messages.success(request,("logged out"))
    return render(request, 'index.html')

# def logout_page(request):
#     return render(request, 'logout.html')

def Customer_Profile(request):
    # Ensure that the user is authenticated
    if not request.user.is_authenticated:
        # Handle the case where the user is not authenticated, e.g., redirect to the login page.
        return redirect('login')  # Replace 'login' with the name of your login view.

    # Get or create the user's profile
    user_profile, created = CustomerProfile.objects.get_or_create(customer=request.user)

    if request.method == 'POST':
        # Handle the POST request for updating user profile fields
        FullName = request.POST.get('fullName')
        street_address=request.POST.get('street_address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        #last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')

        # Update the user profile fields
        user_profile.fullName = FullName
        user_profile.street_address=street_address
        user_profile.country=country
        user_profile.state=state
        user_profile.pincode=pincode
        
        user_profile.phone= phone
        user_profile.save()

        messages.success(request, 'Profile updated successfully')  # Display a success message
        return redirect('Customer_Profile')  # Redirect to the same page or another page after update

    # Handle the GET request for displaying the user profile form
    context = {
        'user_profile': user_profile,
        'form_submitted': False,
    }
    return render(request, 'Customer_Profile.html',context)

def user_home(request):
     return render(request, 'userhome.html')

from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        # Handle the form submission
        product_id = request.POST.get('product-id')
        product_name = request.POST.get('product-name')
        category = request.POST.get('category-name')
        subcategory = request.POST.get('subcategory-name')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount')  # Retrieve as a string
        status = request.POST.get('status')
        product_image = request.FILES.get('product-image')

        price = float(price)

        # Convert discount to a float
        discount = float(discount)

        
        

        # Calculate sale_price
        sale_price = price - (price * (discount / 100))

        # Create a new Product object and save it to the database
        product = Product(
            product_id=product_id,
            product_name=product_name,
            category=category,
            subcategory=subcategory,
            quantity=quantity,
            description=description,
            price=price,
            discount=discount,
            sale_price=sale_price,  # Assign the calculated sale price
            status=status,
            product_image=product_image
        )
        product.save()

        # Redirect to a success page or any other desired action
        return redirect('adminpanel')

    return render(request, 'adminpanel.html')

# def add_product(request):
#     if request.method == 'POST':
#         # Retrieve form data from request.POST
#         product_name = request.POST.get('product_name')
#         category_id = request.POST.get('category_id')
#         subcategory_id = request.POST.get('subcategory_id')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
#         status = request.POST.get('status')

#         # Create a new Product object and save it to the database
#         new_product = Product(
#             product_name=product_name,
#             category_id=category_id,
#             subcategory_id=subcategory_id,
#             price=price,
#             description=description,
#             image=image,
#             status=status
#         )
#         new_product.save()

#         return redirect('adminpanel')  # Redirect to a product list page or another appropriate page

#     return render(request, 'addproduct.html')

# def view_products(request):
#     products = WatchProduct.objects.all()  # Retrieve all products from the database
#     return render(request, 'view_products.html', {'products': products})
def view_product(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'viewproduct.html', {'products': products})

def delete_product(request, product_id):
    if request.method == 'POST':
        # Delete the product from the database
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return redirect('viewproduct')
        except Product.DoesNotExist:
            pass
    return redirect('viewproduct')  # Redirect back to the product list view




def add_to_cart(request):
    # Fetch the product details from your Product model
    products = Product.objects.all()  # This fetches all products; adjust as needed

    # You can pass these products to your template
    return render(request, 'addtocart.html', {'products': products})



# def get_product_details(request):
#     # Retrieve the product details (you can modify this based on your requirements)
#     products = Product.objects.all()
#     product_data = []

#     for product in products:
#         product_data.append({
#             'product_id': product.product_id,
#             'product_name': product.product_name,
#             'category': product.category,
#             'subcategory': product.subcategory,
#             'quantity': product.quantity,
#             'description': product.description,
#             'price': product.price,
#             'discount': product.discount,
#             'sale_price': product.sale_price,
#             'status': product.status,
#             'product_image': product.product_image.url,
#         })

#     return render(request, 'product_details.html', {'products': product_data})

    


def product_details(request, product_id):
    # Retrieve the product details from the database
    product = get_object_or_404(Product, product_id=product_id)

    # Render the product details template with the product data
    return render(request, 'details.html', {'product': product})


def edit_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        # Handle the case where the product doesn't exist
        # You may want to redirect to an error page or take appropriate action
        pass

    if request.method == 'POST':
        # Handle form submission and update the product
        # You can access form data using request.POST and request.FILES
        # Perform validation and update the product data in the database
        # Redirect to a product detail page or a success page

     return render(request, 'edit_product.html', context={'product': product})