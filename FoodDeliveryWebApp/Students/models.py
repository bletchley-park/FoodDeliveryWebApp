from django.db import models

# Create your models here.
class Restaraunt(models.Model):
    restaraunt_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Restaraunt {self.restaraunt_name}'

class MenuItem(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = 'menu_images/')
    category = models.ManyToManyField('Category',related_name='item')
    restaraunt = models.ForeignKey('Restaraunt',on_delete=models.CASCADE)

    def __str__(self) : 
        return self.food_name

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Hostel {self.hostel_name} and ID {self.id}'

class StudentUser(models.Model):
    StudentUser_name = models.CharField(max_length=100)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=100)

    def __str__(self):
        return f'Student User {self.StudentUser_name}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey('StudentUser', on_delete=models.CASCADE)
    restaraunt = models.ForeignKey('Restaraunt', on_delete=models.CASCADE)
    items = models.ManyToManyField('MenuItem',related_name='order',blank = True) 

    def __str__(self):
        return f'Order {self.id} : From {self.restaraunt.restaraunt_name} {self.created_on.strftime("%b %d %I: %M %p")}'
