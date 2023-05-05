from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship

# Create your views here.
def home(request):
    return render(request,'home.html')

def internshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request,"please login to acccess this page")
        return redirect("/auth/login/")
    
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('report')
# converting to upper
        fname=fname.upper()
        femail=femail.upper()
        fusn= fusn.upper()
        fcollege=fcollege.upper()
        foffer=foffer.upper()

        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)
        if check1 or check2:
            messages.warning(request,"Your Details are stored Already")
            return redirect('/intern')
        
        



        query=Internship(name=fname,usn=fusn,email=femail,college_name=fcollege,
                         offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport)
        query.save()
        messages.success(request,"form submitted successfully")
        redirect ('/intern')
        
    return render(request,'intern.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={'posts':posts}
    return render(request,'handleblog.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"thanks for contacting us, we will get by you soon")
      

        return redirect('/contact')
        


    return render(request,'contact.html')