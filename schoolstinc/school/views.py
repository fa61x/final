import simplejson as simplejson
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from school.models import Department, Course, Enquiry


# Create your views here.

def index(request):
    return render(request, "inde1x.html")


def sinup_page(request):
    if request.method == "POST":
        u_name = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username=u_name, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('enquiry')
        else:
            messages.info(request, "invalid user")
            return redirect('reg_page')
    return render(request, "singup.html")


def reg_page(request):
    if request.method == 'POST':
        u_name = request.POST['uname']
        pwd = request.POST['pass1']
        pwd2 = request.POST['pass2']

        if pwd == pwd2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, "username taken")
                return redirect('/reg_page')
            else:
                user = User.objects.create_user(username=u_name, password=pwd)
                user.save();
                print("user created")
                return redirect("/sinup_page")
    else:
        messages.info(request, "password doesn't match ")
        return render(request, 'index.html')


def enquiry(request):
    print("Enter to enquiry Function")
    d = Department.objects.all()
    return render(request, 'enquiry.html', {'d': d})


def save_enq(req):
    if req.method == "POST":
        dp = req.POST.get('department')
        sn = req.POST.get('studentName')
        sx = req.POST.get('gender')
        ag = req.POST.get('age')
        db = req.POST.get('DOB')
        add = req.POST.get('address')
        ph = req.POST.get('phone')
        em = req.POST.get('email')
        crs = req.POST.get('cmbCourse')
        pup = req.POST.get('crses')
        obj = Enquiry(department=dp, email=em, cmbCourse=crs, crses=pup, phone=ph, studentName=sn, gender=sx, age=ag,
                      DOB=db, address=add, )
        obj.save()
    return render('/confirm')



def getCoursedetails(request):
    print("Enter to getCoursedetails Function")
    did = request.GET.get('did', None)
    print(" Dept ID = " + did)
    result_set = []
    select_course = Course.objects.filter(depatment_id=did)
    for w in select_course:
        result_set.append({'id': w.id, 'courseName': w.courseName})
    print(result_set)
    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')


def confirm(req):
    return render(req, "confirm.html")
