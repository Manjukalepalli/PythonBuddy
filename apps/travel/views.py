from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from . models import user,Travel

context ={}

# Create your views here.
def main(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0 #initialize the counter
    return render(request,"travel/index.html",context)

def Registration(request):
    if request.method == 'POST':
        if 'log_errors' in context:
            context.pop("log_errors")
        reg_errors=[]
        reg_errors = user.objects.basic_validator(request.POST)
        username=request.POST['userName']
        if user.objects.filter(Username=username).count()>1:
            reg_errors.append("User Name already exist. Pick different user name")
        if len(reg_errors)==0:
            name=request.POST['name']
            username=request.POST['userName']
            password=request.POST['password']
            user.objects.create(name=name,Username=username,password=password)
            context["username"]=username
            context["user"]=user.objects.get(Username=username)
            print("id for the username is" +str(context["user"].id))
            return redirect('/travel')
        else:
            context["reg_errors"]=reg_errors
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        
        if 'reg_errors' in context:
            context.pop("reg_errors")
        log_errors =[] 
        loginusername=request.POST['loginUsername']
        loginpassword=request.POST['loginpassword']
       
        if user.objects.filter(Username=loginusername).count()!=1:
            log_errors.append("User Name does not exist")
        elif user.objects.filter(Username=loginusername , password=loginpassword).count()!=1:
            log_errors.append("password does not match")

        if len(log_errors)>0:
            context["log_errors"]=log_errors
            return redirect('/')
        context["user"]=user.objects.get(Username=loginusername)
        context["username"]=loginusername
        return redirect('/travel')
    else:
        return redirect('/')
  
def travel(request):
    context["Current_user_travels"]=user.objects.get(id=context["user"].id).Travels.all()
    context["other_plans"]=Travel.objects.all().exclude(books=context["user"].id)
    return render(request,"travel/travel.html",context)

def addplan(request):
    return render(request,"travel/addplan.html",context)

def addnewplan(request):
    if request.method == 'POST':
        traval_errors=[]
        traval_errors = Travel.objects.travel_validation(request.POST)
        if len(traval_errors)>0:
            context["traval_errors"]=traval_errors
            return redirect('/addplan')
        else:
            destination=request.POST['destination']
            description=request.POST['description']
            start_date=request.POST['start_date']
            end_date=request.POST['end_date']
            creator=user.objects.get(Username=context["username"])
            Travel.objects.create(destination=destination,description=description,start=start_date,end=end_date,creator=creator)
            traverlor=Travel.objects.get(destination=destination,creator=creator)
            traverlor.books.add(creator)
    return redirect('/travel')

def add_plan_to_user(request,travel_id):
    print(context["username"])
    creator=user.objects.get(Username=context["username"])
    traverlor=Travel.objects.get(id=travel_id)
    traverlor.books.add(creator)
    return redirect('/travel')

def show(request, travel_id):
    traveldetials= Travel.objects.get(id=travel_id)
    context["traveldetials"]=traveldetials
    context["user"]=traveldetials.creator
    context["otheruser"]=user.objects.filter(Travels=travel_id).exclude(id=context["user"].id)
    return render(request, 'travel/showdetail.html', context)    