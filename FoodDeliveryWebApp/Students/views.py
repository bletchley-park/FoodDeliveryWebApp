from django.shortcuts import render
from django.views import View
from .models import OrderModel, StudentUser
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

        context = {
            'student': student,
            'orders': orders,
        }
        return render(request, 'Students/orders.html', context)

