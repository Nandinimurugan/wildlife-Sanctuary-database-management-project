from django.db import models
from django.core.urlresolvers import reverse

class Animal(models.Model):
    id=models.AutoField(primary_key=True)
    Animal_species=models.CharField(max_length=100)
    Animal_count=models.IntegerField(default=0)
    Animal_type=models.CharField(max_length=20)
    Scientific_name=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    Animal_feed=models.CharField(max_length=100)
    Feed_cost=models.FloatField(default=0)
    Animal_image=models.FileField(null=True,blank=True)
 
    def get_absolute_url(self):
        return reverse('animal_details:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.id)+' - '+(self.Animal_species)

class Medicine(models.Model):
    Animal_id=models.ForeignKey(Animal,on_delete=models.CASCADE)
    Medicine_name=models.CharField(max_length=200)
    Medicine_cost=models.FloatField(default=0.0)
    Date=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('animal_details:med-detail')

    def __str__(self):

        return str(self.Animal_id)+' on '+str(self.Date)

class Accounts(models.Model):
    id=models.AutoField(primary_key=True)
    Date=models.DateField(auto_now=True)
    Income=models.FloatField(default=0.0)
    Expenditure=models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('animal_details:acc-detail')

    def __str__(self):
        return str(self.id)+' on '+str(self.Date)

class Organisation_grants(models.Model):
    id=models.AutoField(primary_key=True)
    Organisation_name=models.CharField(max_length=200)
    Organisation_phno=models.CharField(max_length=20)
    Address=models.CharField(max_length=300)
    Amount=models.FloatField(default=0.0)
    Date=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('animal_details:grant-detail',kwargs={'pk':self.pk})

    def __str__(self):
         return str(self.Organisation_name)+' - '+(self.Amount)



class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    Staff_Name=models.CharField(max_length=100)
    Designation=models.CharField(max_length=50)
    Salary=models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('animal_details:Staff-detail')

    def __str__(self):
         return str(self.id)+' - '+self.Staff_Name


class Tourists(models.Model):
    id=models.AutoField(primary_key=True)
    Tourists_name=models.CharField(max_length=100)
    Donation=models.FloatField(default=0.0)
    Date=models.DateField(auto_now=True)
    GuideName=models.CharField(max_length=100)
    Phone_number=models.IntegerField(default=0)
    Entryfee=models.IntegerField(default=200)


    def get_absolute_url(self):
        return reverse('animal_details:Tourist-detail')

    def __str__(self):
         return str(self.id)+' - '+(self.Tourists_name)

   