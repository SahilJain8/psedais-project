from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.
class Service(models.Model):
    category = models.CharField(max_length=100,default='Hair Services')
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    image = models.ImageField(upload_to='service_images/', null=True)
    duration = models.DurationField()

    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class StaffMember(models.Model):
    name = models.CharField(max_length=50)
    branches = models.ManyToManyField(Branch)
    image = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=100,null=True)
    address = models.TextField()
    def __str__(self):
        return self.name
<<<<<<< HEAD
class Packages(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED')
    services = models.ManyToManyField(Service)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    

=======
# class Appointment(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
#     staff_member = models.ForeignKey(StaffMember, on_delete=models.PROTECT)
#     services = models.ManyToManyField(Service)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     status = models.CharField(max_length=220, null=True)
#     cancel_time = models.TimeField(null=True, blank=True)
#     cancellation_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
#     discounted_price = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',null = True)
#     amount_to_be_paid = MoneyField(max_digits=14,decimal_places=2,default_currency='AED',null = True)
#     date = models.DateField(null=True)
#     branch = models.ForeignKey('Branch', on_delete=models.PROTECT,null=True)
#     tips = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',default=0.00)
#     def __str__(self):

        
#         return f"{self.customer} - {self.services} with {self.staff_member} on {self.start_time}"
>>>>>>> 8250d3245bda2620aa2a8a7ea3759537e698c007
class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.PROTECT)
    services = models.ManyToManyField(Service)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=220, null=True)
    cancel_time = models.TimeField(null=True, blank=True)
    cancellation_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    discounted_price = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',null = True)
    amount_to_be_paid = MoneyField(max_digits=14,decimal_places=2,default_currency='AED',null = True)
    date = models.DateField(null=True)
    branch = models.ForeignKey('Branch', on_delete=models.PROTECT,null=True)
    tips = MoneyField(max_digits=12,decimal_places=2,default_currency='AED',default=0.00)
    def _str_(self):

        
        return f"{self.customer} - {self.services} with {self.staff_member} on {self.start_time}"
<<<<<<< HEAD


class Invoice(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT)
    
    tax = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    discounted_price = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    tips = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    price_to_be_paid = MoneyField(max_digits=14, decimal_places=2, default_currency='AED',null = True)
    
    
=======
>>>>>>> 8250d3245bda2620aa2a8a7ea3759537e698c007
