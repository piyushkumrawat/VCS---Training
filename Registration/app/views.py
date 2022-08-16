from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import form

def reg(request):
    if request.method=="POST":
        name=request.POST['fname']
        email=request.POST['email']
        password=request.POST['Password']
        reg=form(name=name, email=email, password=password)
        reg.save()
        return render(request,"login.html")
    else:
        pass
    return render(request,"reg.html")

def log(request):
    try:
        if request.method=="POST":
            username=request.POST['fname']
            password=request.POST['Password']
            user=form.objects.filter(name=username,password=password)
            k=user[0]
            if k is not None:
                return HttpResponseRedirect("/done/")
        else:
            return render(request,"login.html")
    except:                
       return render(request,"login.html")

def done(request):
    return render(request,'done.html')

