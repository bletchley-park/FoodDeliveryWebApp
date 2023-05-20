from django.db import models

# Create your models here.
class Restaraunt(models.Model):
    restaraunt_name = models.CharField(max_length=100)
    restaraunt_address = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Restaraunt {restaraunt_name} and ID {restaraunt_id}'

class MenuItem(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    name = models.CharField(max_length = 100) #food_type
    image = models.ImageField(upload_to = 'menu_images/')
    category = models.ManyToManyField('Category',related_name='item')
    restaraunt = models.ManyToManyField('Restaraunt',related_name='food_restaraunt')

    def __str__(self) : 
        return self.name

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Hostel {hostel_name} and ID {hostel_id}'

class StudentUser(models.Model):
    StudentUser_name = models.CharField(max_length=100)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    student = models.ForeignKey('StudentUser', on_delete=models.CASCADE)
    restaraunt = models.ForeignKey('Restaraunt', on_delete=models.CASCADE)
    items = models.ManyToManyField('MenuItem',related_name='order',blank = True) 

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
