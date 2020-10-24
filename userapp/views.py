from django.shortcuts import render, redirect
from userapp.forms import UserRegisterForm
from userapp.models import Usertable
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import logout  # for userdefined logout operation  ### most important line
from userapp.decorators import user_login_required
from adminapp.models import Address, ITJobs, MechJobs, CivilJobs
from django.contrib.auth.models import User

#-------------------------------------------------------------------------------#
def user_login_register_view(request):
    return render(request, 'userloginregister.html')

    ### Registration Operation ####
class UserFormView(CreateView):
    form_class = UserRegisterForm   # form.py ka classname ka class
    model = Usertable
    template_name = 'userregister.html'
    success_url = '/userlogin/'

    ### Logout Operation ####
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('/userlogin/')

#======================================================================================#
            ####  IT OPERATIONS ####
#======================================================================================#
    ### Login Operation & Decorator Operations (By Using Sessions) ####
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Usertable.objects.get(username=username, password=password)
            print(user)
            if user is not None: # user is present
                request.session['user'] = user.username
                request.session['user_id'] = user.id   # SESSION SET ,humne session ko set kiya hai
                return redirect('/readit/')
            else:
                messages.error(request,'Please enter valid username and password')
                return redirect('/userlogin/')
        except Exception:
            messages.error(request,'Please enter valid username and password')
            return redirect('/userlogin/')
    return render(request, 'userlogin.html')

    #### READ OPERATIONS ####
@user_login_required
def readuserit_view(request):
    data = ITJobs.objects.all()
    return render(request,'readit.html', {'data':data})

    #### USER APPLYING FOR THE IT JOB ####
@user_login_required
def it_apply(request,*args,**kwargs): #swapnesh ---> {id : value ---> 13}
    jobid =kwargs.get('id') # ye id se job ki value milegi. kwargs means dict-->{key:value}
    if jobid:
        obj = ITJobs.objects.get(pk=jobid)  # recruiter ki job id le liya, ye id se particular object fetch kiya -->jobid =kwargs.get('id')
        user_id = request.session.get('user_id') # session.get jab user login hoga toh uske session ka id milega (get hoga)
        uobj = Usertable.objects.get(pk=user_id)  # user ki job id le liya, user_id = request.session.get('user_id')
        obj.user.add(uobj)  # user ---> It is an adminapp models.py parameter, add method is applicable to ManyToManyField(database realationship)
        print(obj.user.all()) # ye job par kitne users ne apply kiya hai
        obj.save()
        messages.success(request, 'You have applied successfully')
        return redirect('/readit/')
    return redirect('/readit/')

#======================================================================================#
            ####  MECHANICAL OPERATIONS ####
#======================================================================================#

        ### Login Operation (By Using Sessions) ####
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Usertable.objects.get(username=username, password=password)
            print(user)
            if user is not None:
                request.session['user'] = user.username
                request.session['user_id'] = user.id   # SESSION SET ,humne session ko set kiya hai
                return redirect('/readmech/')
            else:
                messages.error(request,'Please enter valid username and password')
                return redirect('/userlogin/')
        except Exception:
            messages.error(request,'Please enter valid username and password')
            return redirect('/userlogin/')
    return render(request, 'userlogin.html')

    #### READ OPERATIONS ####
@user_login_required
def readusermech_view(request):
    data = MechJobs.objects.all()
    return render(request,'readmech.html', {'data':data})

    #### USER APPLYING FOR THE Mech JOB ####
@user_login_required
def mech_apply(request,*args,**kwargs): #swapnesh ---> {id : value ---> 13}
    jobid =kwargs.get('id') # ye id se job ki value milegi. kwargs means dict-->{key:value}
    if jobid:
        messages.success(request, 'You have applied successfully')
        obj = MechJobs.objects.get(pk=jobid)  # ye id se particular object fetch kiya -->jobid =kwargs.get('id')
        user_id = request.session.get('user_id') # SESSION GET jab user login hoga toh uske session ka id milega (get hoga)
        uobj = Usertable.objects.get(pk=user_id)
        obj.user.add(uobj)  # user ---> It is an adminapp models.py parameter, add method is applicable to ManyToManyField(database realationship)
        print(obj.user.all()) # ye job par kitne users ne apply kiya hai
        obj.save()
        return redirect('/readmech/')
    return redirect('/readmech/')

#======================================================================================#
            ####  CIVIL OPERATIONS ####
#======================================================================================#

        ### Login Operation (By Using Sessions) ####
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Usertable.objects.get(username=username, password=password)
            print(user)
            if user is not None:
                request.session['user'] = user.username
                request.session['user_id'] = user.id   # SESSION SET ,humne session ko set kiya hai
                return redirect('/readcivil/')
            else:
                messages.error(request,'Please enter valid username and password')
                return redirect('/userlogin/')
        except Exception:
            messages.error(request,'Please enter valid username and password')
            return redirect('/userlogin/')
    return render(request, 'userlogin.html')

    #### READ OPERATIONS ####
@user_login_required
def readusercivil_view(request):
    data = CivilJobs.objects.all()
    return render(request,'readcivil.html', {'data':data})

    #### USER APPLYING FOR THE Civil JOB ####
@user_login_required
def civil_apply(request,*args,**kwargs): #swapnesh ---> {id : value ---> 13}
    jobid =kwargs.get('id') # ye id se job ki value milegi. kwargs means dict-->{key:value}
    if jobid:
        messages.success(request, 'You have applied successfully')
        obj = CivilJobs.objects.get(pk=jobid)  # ye id se particular object fetch kiya -->jobid =kwargs.get('id')
        user_id = request.session.get('user_id') # SESSION GET jab user login hoga toh uske session ka id milega (get hoga)
        uobj = Usertable.objects.get(pk=user_id)
        obj.user.add(uobj)  # user ---> It is an adminapp models.py parameter, add method is applicable to ManyToManyField(database realationship)
        print(obj.user.all()) # ye job par kitne users ne apply kiya hai
        obj.save()
        return redirect('/readcivil/')
    return redirect('/readcivil/')
