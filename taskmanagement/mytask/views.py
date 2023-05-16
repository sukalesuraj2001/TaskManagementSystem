from django.shortcuts import render,redirect
from django.http import HttpResponse
from mytask.models import MyTask
from django.db.models import Q
from mytask.forms import UserForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def home(request):
    return render(request,'index.html')

   
def addtask(request):
    if request.method == 'POST':
        t = request.POST['title']
        d = request.POST['desc']
        s = request.POST['status']
        sd=request.POST['sdate']
        ed=request.POST['edate']
       
        

        task = MyTask.objects.create(task_title=t, desc=d, status=s,sdate=sd,edate=ed)
        task.save()

        return  redirect('/addtask')
    else:
     
     data=MyTask.objects.all()
   
     content={}
     content['tasks']=data
    
     return render(request,'addtask.html',content)
   


# =========================delete task =============================

def deletetask(request,rid):
    # print("ID to be deleted:",rid)
    data=MyTask.objects.filter(id=rid)
    data.delete()
    return redirect('/viewtask')
# =========================edit product================


def edittask(request,rid):
      if request.method=='POST':

        # print('id to be edited',rid)
       n=request.POST['title']
       d=request.POST['desc']
        #  st=request.POST['sdate']
       #  e=request.POST['edate']
       
       s=request.POST['status']
      
       



       p=MyTask.objects.filter(id=rid)
       p.update(task_title=n,desc=d,status=s)
       
       return  redirect('/viewtask')

        
      
      else: 
       data=MyTask.objects.filter(id=rid)
       content={}
       content['tasks']=data
       return render(request,'edittask.html',content)
      




# =====================view tasks=====================

def viewtask(request):
   data=MyTask.objects.all()
   content={}
   content['tasks']=data
   
   return render(request,'viewtask.html',content)


#============ filter by all tasks==============================

def alltask(request,sv):
   if sv==0:
      data=MyTask.objects.filter(status=1)
      content={}
      content['tasks']=data
   
      return render(request,'viewtask.html',content)
   else:
      data=MyTask.objects.filter(status=1)
      content={}
      content['tasks']=data
   
      return render(request,'viewtask.html',content)
      
def pending(request,sv):
   if sv==1:
      data=MyTask.objects.filter(status=1)
      content={}
      content['tasks']=data
   
      return render(request,'viewtask.html',content)
   else:
      data=MyTask.objects.filter(status=0)
      content={}
      content['tasks']=data
   
      return render(request,'viewtask.html',content)
   

   # ==============User register==============

def user_register(request):
   content={}
   reobj=UserForm()
   content['userform']=reobj
   if request.method=='POST':
      reobj=UserForm(request.POST)
      if reobj.is_valid():
         reobj.save()
         content['success']='User Created Sucessfully'
         return render(request,'user_register.html',content)
   else:
         return render(request,'user_register.html',content)


def user_login(request):
    if request.method=='POST':
        dataobj=AuthenticationForm(request=request,data=request.POST)
        print(dataobj) 
        if dataobj.is_valid():
         uname=dataobj.cleaned_data['username']
         upass=dataobj.cleaned_data['password']
         print(uname)
         print(upass)
         u=authenticate(username=uname,password=upass)
         print(u) 
        if u:
            login(request,u)
            return redirect('/')
    else:
        eobj=AuthenticationForm()
        content={} 
        content['loginform']=eobj
        return render(request,'user_login.html',content)


def user_logout(request):
    logout(request)
    return redirect('/login')
         
         