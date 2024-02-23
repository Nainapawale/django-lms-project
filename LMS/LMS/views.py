from django.shortcuts import redirect,render
from app.models import Categories,Course

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    categories = Categories.objects.all().order_by('id')[0:6]
    course=Course.objects.filter(status='PUBLISH').order_by('id')
    print(course)
    context = {
        'categories': categories,
        'course':course,
    }
    # print(categories)  # Corrected the variable name

    return render(request, 'Main/home.html',context)

def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')

def CONTACT_US(request):
    return render(request,'Main/contact_us.html')

def ABOUT_US(request):
    return render(request,'Main/about_us.html')