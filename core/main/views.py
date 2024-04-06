from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import *
from .models import *

# Create your views here.


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched1 = request.POST['searched']

        searched = ShopProduct.objects.filter(name__icontains=searched)
        searched1 = Product.objects.filter(name__icontains=searched1)


        if not searched and not searched1:
            messages.success(request, "That Product Does Not Exsist In Our Shop. Please try Again")
            return render(request, 'search.html', {})
        if searched:
            return render(request, 'search.html', {'searched':searched}) 
        if searched1:
            return render(request, 'search.html', {'searched1':searched1})

    else:
        return render(request, 'search.html', {})
    

    
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homes = Home.objects.all()
        product = HomeProduct.objects.all()
        product1 = HomeProduct1.objects.all()
        product2 = HomeProduct2.objects.all()
        cats = Category.objects.all()
        cats2 = Category2.objects.all()
        cats3 = Brand.objects.all()
        return render(request, self.template_name, {'homes':homes, 
                                                    'product':product, 
                                                    'product1':product1,
                                                    'product2':product2,
                                                    'cats':cats,
                                                    'cats2':cats2,
                                                    'cats3':cats3
                                                    })


class ShopListView(ListView):
    template_name = 'shops.html'

    def get(self, request):
        shops = ShopProduct.objects.all()
        return render(request, self.template_name, {'shops':shops})
    

class ShopDetailView(DetailView):
    template_name = 'shop_detail.html'

    def get(self, request, id):
        shop = ShopProduct.objects.get(pk=id)
        return render(request, self.template_name, {'shop':shop})




class ErorListView(ListView):
    template_name = '404.html'
    
    def get(self, request):
        eror = Eror404.objects.all()
        return render(request, self.template_name,{'eror':eror})




class CheckoutListView(ListView):
    template_name = 'checkout.html'
    
    def get(self, request):
        checkouts = Checkout.objects.all()
        return render(request, self.template_name,{'checkouts':checkouts})



class FooterListView(ListView):
    template_name = 'base.html'
    
    def get(self, request):
        footers = Footer.objects.all()
        return render(request, self.template_name,{'footers':footers})




class ProductListView(ListView):
    template_name = 'product_detail.html'

    def get(self, request):
        prods = Product.objects.all()
        return render(request, self.template_name,{'prods':prods})
    


class ProductDetailView(DetailView):
    template_name = 'detail_detail.html'

    def get(self, request, id):
        prod = Product.objects.get(pk=id)
        return render(request, self.template_name, {'prod':prod})




class BlogListView(ListView):
    template_name = 'blog_list.html'
    
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, self.template_name,{'blogs':blogs})



class BlogSingleListView(ListView):
    template_name = 'blog_single.html'
    
    def get(self, request):
        blogsing = BlogSingle.objects.all()
        blogsing2 = BlogSingle2.objects.all()
        return render(request, self.template_name,{'blogsing':blogsing, 'blogsing2':blogsing2})





class CartListView(ListView):
    template_name = 'cart.html'
    
    def get(self, request):
        carts = Cart.objects.all()
        return render(request, self.template_name,{'carts':carts})


def contact(request):
    return render(request, 'contact.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f'You Have Been Logged In Successfully. Welcome! {username} '))
            return redirect('home')
        else:
            messages.success(request, ("Something went wrong username or password is wrong, Please try again!"))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f"You Have Register Successfully!! Welcome! {username} "))
            return redirect('home')
        else:
            messages.success(request, ("Oops! There was a problem Registering, please try again."))
            return redirect('register')

    else:
        return render(request, 'register.html', {'form':form})