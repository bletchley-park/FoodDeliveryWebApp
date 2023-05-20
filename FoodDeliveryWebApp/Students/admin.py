from django.contrib import admin
from .models import MenuItem, Category, OrderModel , Restaraunt, Hostel, StudentUser

admin.site.register(StudentUser)
admin.site.register(Restaraunt)
admin.site.register(Hostel)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
# Register your models here.
