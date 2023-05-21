from django.shortcuts import render
from django.views import View
from .models import OrderModel, StudentUser, Restaraunt, MenuItem
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Students/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Students/about.html')

class StudentOrdersView(View):
    def get(self, request, student_id):
        student = StudentUser.objects.get(id=student_id)
        orders = student.ordermodel_set.all()
        total_price = 0
        for order in orders:
            items = order.items.all()
            order_price = sum(item.price for item in items)
            total_price += order_price

        context = {
            'student': student,
            'orders': orders,
            'totalprice': total_price
        }
        return render(request, 'Students/orders.html', context)

class RestaurantMenuView(View):
    def get(self, request):
        restaurants = Restaraunt.objects.all()
        
        context = {
            'restaurants': restaurants
        }
        
        return render(request, 'Students/menu.html', context)
    
    def post(self, request):
        restaurant_id = request.POST.get('restaurant')
        restaurant = Restaraunt.objects.get(id=restaurant_id)
        menu_items = MenuItem.objects.filter(restaraunt=restaurant)
        
        context = {
            'restaurant': restaurant,
            'menu_items': menu_items
        }

        print(context)
        
        return render(request, 'Students/menu_items.html', context)

