from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from .models import Animal,Medicine,Accounts,Organisation_grants,Staff,Tourists
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import  UserForm
from django.shortcuts import render,get_object_or_404
from django.conf import settings



user=authenticate(username='a',password='1')

from django.db.models import Sum


def add_account(request):
     acc=Accounts()
     don=Tourists.objects.aggregate(Sum('Donation'))
     amt=Organisation_grants.objects.aggregate(Sum('Amount'))
     acc.Income=don['Donation__sum']+amt['Amount__sum']
     sal=Staff.objects.aggregate(Sum('Salary'))
     med=Medicine.objects.aggregate(Sum('Medicine_cost'))
     feed=Animal.objects.aggregate(Sum('Feed_cost'))
     acc.Expenditure=sal['Salary__sum']+med['Medicine_cost__sum']+feed['Feed_cost__sum']
     acc.save()
     new_account=Accounts.objects.all()
     return render(request, 'animal_details/account.html', {'new_account':new_account})

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                animal=Animal.objects.all()
               
                return render(request, 'animal_details/index1.html', {'animals': animal})
    context = {
        "form": form,
    }
    return render(request, 'animal_details/register.html', context)


def home(request):
   
    return render(request,'animal_details/home.html')




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                animal=Animal.objects.all()
               
                return render(request, 'animal_details/index1.html', {'animals': animal})
               
            else:
                return render(request, 'animal_details/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'animal_details/login.html', {'error_message': 'Invalid login'})
    return render(request, 'animal_details/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'animal_details/home.html', context)



def index(request):
    if not request.user.is_authenticated():
        return render(request, 'animal_details/login.html')
    else:
        animal=Animal.objects.all()
        return render(request, 'animal_details/index1.html', {'animals': animal})
               

def med_detail(request):
    if not request.user.is_authenticated():
        return render(request, 'animal_details/login.html')
    else:
        medicine=Medicine.objects.all()
        return render(request, 'animal_details/med.html', {'medicines':medicine})





               








class DetailView(LoginRequiredMixin,generic.DetailView):
     login_url =None
     
     redirect_unauthenticated_users=False
     raise_exception=False
   
     model = Animal
     template_name = 'animal_details/detail.html'


     


   
#-----------------------------------------------------------------------------------------------------------------------

class AnimalCreate(LoginRequiredMixin,CreateView):

    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
    model = Animal
    fields = ['id', 'Animal_species', 'Animal_count', 'Animal_type', 'Scientific_name', 'Country', 'Animal_feed','Feed_cost','Animal_image']

class AnimalUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Animal
    fields = ['id', 'Animal_species', 'Animal_count', 'Animal_type', 'Scientific_name', 'Country', 'Animal_feed','Feed_cost']

class AnimalDelete(LoginRequiredMixin,DeleteView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model =Animal
    success_url = reverse_lazy('animal_details:index')

class MedicineDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Medicine
    template_name = 'animal_details/med.html'

class MedicineCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Medicine
    fields = ['Animal_id', 'Medicine_name', 'Medicine_cost']

class MedicineUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Medicine
    fields = ['Animal_id', 'Medicine_name', 'Medicine_cost']

#-----------------------------------------------------------------------------------------------------------------------

class AccountCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    fields=['Income','Expenditure']

class AccountUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    fields=['Income','Expenditure']

class AccountDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    template_name='animal_details/acc.html'

    def get_queryset(self):
        return Accounts.objects.all()

class GrantsCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsUpdate(UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    template_name='animal_details/grant.html'
#-----------------------------------------------------------------------------------------------------------------------
#staff
class StaffCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Staff
    fields = ['id','Staff_Name','Designation','Salary']
class StaffUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Staff
    fields = ['id','Staff_Name','Designation','Salary']

class StaffDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model =Staff
    template_name='animal_details/staff.html'

    def get_queryset(self):
        return Staff.objects.all()

class StaffDelete(LoginRequiredMixin,DeleteView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Staff
    success_url = reverse_lazy('animal_details:Staff-detail')




#tourist
class TouristCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Tourists
    fields = ['id','Tourists_name','Donation','GuideName','Phone_number','Entryfee']

class TouristUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Tourists
    fields = ['id','Tourists_name','Donation','GuideName','Phone_number','Entryfee']
class TouristDelete(LoginRequiredMixin,DeleteView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Tourists
    success_url = reverse_lazy('tourists_details:index')
class TouristDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Tourists
    template_name='animal_details/tourists.html'



class AccountCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    fields=['Income','Expenditure']

class AccountUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    fields=['Income','Expenditure']

class AccountDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Accounts
    template_name='animal_details/acc.html'

    def get_queryset(self):
        return Accounts.objects.all()

class AccountDelete(LoginRequiredMixin,DeleteView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model =Accounts
    success_url = reverse_lazy('animal_details:acc-detail')


class GrantsCreate(LoginRequiredMixin,CreateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsUpdate(LoginRequiredMixin,UpdateView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    fields=['id','Organisation_name','Organisation_phno','Address','Amount']

class GrantsDetail(LoginRequiredMixin,generic.ListView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model=Organisation_grants
    template_name='animal_details/grant.html'

    def get_queryset(self):
        return Organisation_grants.objects.all()

class GrantsDelete(LoginRequiredMixin,DeleteView):
    login_url =None
     
    redirect_unauthenticated_users=False
    raise_exception=False
   
    model = Organisation_grants
    success_url = reverse_lazy('animal_details:grant-detail')
