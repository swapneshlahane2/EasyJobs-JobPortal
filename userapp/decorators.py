from django.shortcuts import render, redirect


def user_login_required(function):
    def wrap(request,*args,**kwargs):
        #print(request.session.get('user'))
        if request.session.get('user'):
            return function(request,*args,**kwargs)
        else:
            return redirect('/userlogin/')
    return wrap
