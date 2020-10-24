from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from adminapp.forms import SignupForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from adminapp.models import Address, ITJobs, MechJobs, CivilJobs
from userapp.models import Usertable
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required   # this is only applicable to function base view
from django.utils.decorators import method_decorator  # this is  applicable to class base view
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return HttpResponse('<center><h1>Your Feedback has been submitted successfully.</h1></center>')

def loginregister_view(request):
    return render(request, 'loginregister.html')

@login_required(login_url ='/login/')
def choose_view(request):
    return render(request,'choose.html')

    #### REGISTRATION OPERATION ####
def admin_register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'admin_register.html', {'form':form})

    #### CREATE ADDRESS OPERATION ####
@method_decorator(login_required, name='dispatch')   # after this go to settings.py file and redirect --->LOGIN_URL = 'login'
class AddAddressView(CreateView):
    model = Address
    template_name = 'address.html'
    fields = "__all__"

#======================================================================================================#
            #### IT JOB OPERATIONS ####
#======================================================================================================#
    #### CREATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')   # after this go to settings.py file and redirect --->LOGIN_URL = 'login'
class AddITJobView(CreateView):
    model = ITJobs
    template_name = 'additjob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    def form_valid(self,form):
        form.instance.hrtable = self.request.user # current login user
        return super().form_valid(form)

    #### READ JOB OPERATION ####
@login_required(login_url ='/login/')
def readit_view(request,id):
    user = User.objects.get(pk=id)  # particular user id
    obj = ITJobs.objects.filter(hrtable__username=user.username)   # OR (hrtable__username=user)
    print(user, obj)
    return render(request, 'readitjob.html',{'obj':obj})

    #### DELETE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class DeleteITJobView(DeleteView):
    model = ITJobs
    template_name = 'deleteitjob.html'
    def get_success_url(self):  # this fucntion is used to redirect on particular user id
        return reverse('readitjob', kwargs= {'id':self.request.user.id}) # this is used to redirect on particular user id

    #### UPDATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class UpdateITJobView(UpdateView):
    model = ITJobs
    template_name = 'updateitjob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    #### SHOW APPLIED RESUME BY USER ####
@login_required(login_url ='/login/')
def resume_it(request,id):
    itjobs = ITJobs.objects.get(pk=id)  # particular id
    users = itjobs.user.all()  # all the applicants applied on the particular  job id (above id)
    return render(request,'resumeit.html',{'users':users})

#======================================================================================================#
            #### MECHANICAL JOB OPERATIONS ####
#======================================================================================================#

    #### CREATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')   # after this go to settings.py file and redirect --->LOGIN_URL = 'login'
class AddMechJobView(CreateView):
    model = MechJobs
    template_name = 'addmechjob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    def form_valid(self,form):
        form.instance.hrtable = self.request.user # current login user
        return super().form_valid(form)

    #### READ JOB OPERATION ####
@login_required(login_url ='/login/')
def readmech_view(request,id):
    user = User.objects.get(pk=id)
    obj = MechJobs.objects.filter(hrtable__username=user.username)
    print(user, obj)
    return render(request, 'readmechjob.html',{'obj':obj})

    #### DELETE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class DeleteMechJobView(DeleteView):
    model = MechJobs
    template_name = 'deletemechjob.html'
    def get_success_url(self):
        return reverse('readmechjob', kwargs= {'id':self.request.user.id})

    #### UPDATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class UpdateMechJobView(UpdateView):
    model = MechJobs
    template_name = 'updatemechjob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    #### SHOW APPLIED RESUME BY USER ####
@login_required(login_url ='/login/')
def resume_mech(request,id):
    mechjobs = MechJobs.objects.get(pk=id)
    users = mechjobs.user.all()
    return render(request,'resumemech.html',{'users':users})

#======================================================================================================#
            #### CIVIL JOB OPERATIONS ####
#======================================================================================================#

    #### CREATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')   # after this go to settings.py file and redirect --->LOGIN_URL = 'login'
class AddCivilJobView(CreateView):
    model = CivilJobs
    template_name = 'addciviljob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    def form_valid(self,form):
        form.instance.hrtable = self.request.user # current login user
        return super().form_valid(form)

    #### READ JOB OPERATION ####
@login_required(login_url ='/login/')
def readciviljob_view(request,id):
    user = User.objects.get(pk=id)
    obj = CivilJobs.objects.filter(hrtable__username=user.username)
    print(user, obj)
    return render(request, 'readciviljob.html',{'obj':obj})

    #### DELETE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class DeleteCivilJobView(DeleteView):
    model = CivilJobs
    template_name = 'deleteciviljob.html'
    def get_success_url(self):
        return reverse('readciviljob', kwargs= {'id':self.request.user.id})

    #### UPDATE JOB OPERATION ####
@method_decorator(login_required, name='dispatch')
class UpdateCivilJobView(UpdateView):
    model = CivilJobs
    template_name = 'updateciviljob.html'
    fields = ['id','company','title','desgination','experience','package','vaccancy','date_from','date_to','location']

    #### SHOW APPLIED RESUME BY USER ####
@login_required(login_url ='/login/')
def resume_civil(request,id):
    civiljobs = CivilJobs.objects.get(pk=id)
    users = civiljobs.user.all()
    return render(request,'resumecivil.html',{'users':users})
