from django.shortcuts import *
from .models import *

# Create your views here.
def IndexPage(request):
    return render(request,"crudapp/index.html")

def registeruser(request):
    username=request.POST['Username']
    email=request.POST['Email']
    password=request.POST['Password']
  
    newuser=User.objects.create(Username=username,Email=email,Password=password)
    return HttpResponseRedirect(reverse('showdata'))

def show(request):
    one_user=User.objects.all()
    return render(request,"crudapp/showdata.html",{'key1':one_user})

def Edit(request):
    n=request.POST['u']
    all_user=User.objects.filter(id=n)
    return render(request,"crudapp/edit.html",{'key':all_user})

def change(request):
    c1 = True
    c2 = True
    c3 = True
    U = request.POST['Username']
    e = request.POST['Email']
    p = request.POST['Password']
    u = request.POST['id']

    n = User.objects.get(id=u)
    
    if(U==""):
        c1  = False
    if(e==""):
        c2  = False
    if(p==""):
        c3  = False

    if(c1 == True):
        n.Username = U
        n.save()
    if(c2 == True):
        n.Email = e
        n.save()
    if(c3 == True):
        n.Password = p
        n.save()
    
    all_user= User.objects.all()

    return render(request,"curdapp/done.html",{'key':all_user})

def del_user(request):
    n = request.POST['g']
    all_user = all.objects.get(id=n)
    all_user.delete()
    one_user = User.objects.all()
    return render(request,"curdapp/showdata.html",{'key1':one_user})