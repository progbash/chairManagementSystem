from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Chair, Specialty, Specialization, Teacher, Article, CGroup, Student

def index(request):
    context = {
        'articles': Article.objects.all()
    }

    return render(request, 'articles.html', context)


def article(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id)
    }
    
    return render(request, 'article.html', context)


def chairs(request):
    template = loader.get_template('chairs.html')
    context = {
        'chairs_list' : Chair.objects.all()
    }
    return HttpResponse(template.render(context, request))


def list_of_specialties(request, chair_id):
    chairs = Chair.objects.all()

    if chair_id:
        chair_id = get_object_or_404(Chair, id=chair_id)
        bachelor_sp = Specialty.objects.filter(degree_id=1, chair_id=chair_id) 
        master_sp = Specialty.objects.filter(degree_id=2, chair_id=chair_id)
        phd_sp = Specialty.objects.filter(degree_id=3, chair_id=chair_id) 

    context = {
        'chairs': chairs,
        'chair_id': chair_id,
        'bachelor_sp': bachelor_sp,
        'master_sp': master_sp,
        'phd_sp': phd_sp,
    }
    return render(request, 'specialties.html', context)


def list_of_specializations(request, specialty_id):
    specialties = Specialty.objects.all()

    if specialty_id:
        specialty_id = get_object_or_404(Specialty, id=specialty_id)
        specializations = Specialization.objects.filter(specialty_id=specialty_id)
    
    context = {
        'specialties': specialties,
        'specialty_id': specialty_id,
        'specializations': specializations
    }
    return render(request, 'specializations.html', context)

def list_of_teachers(request, chair_id):
    chairs = Chair.objects.all()

    if chair_id:
        chair_id = get_object_or_404(Chair, id=chair_id)
        teachers = Teacher.objects.filter(chair_id=chair_id)
    
    context = {
        'chairs': chairs,
        'chair_id': chair_id,
        'teachers': teachers
    }
    return render(request, 'teachers.html', context)
    

def list_of_groups(request, chair_id, specialty_id):
    chairs = Chair.objects.all()

    if specialty_id:
        chair_id = get_object_or_404(Chair, id=chair_id)
        specialty_id = get_object_or_404(Specialty, id=specialty_id)
        groups = CGroup.objects.filter(specialty_id=specialty_id)
    
    context = {
        'groups': groups,
        'chairs': chairs,
        'chair_id': chair_id,
    }
    return render(request, 'groups.html', context)


def list_of_students(request, chair_id, specialty_id):
    chairs = Chair.objects.all()

    if specialty_id:
        chair_id = get_object_or_404(Chair, id=chair_id)
        specialty_id = get_object_or_404(Specialty, id=specialty_id)
        students = Student.objects.filter(specialty_id=specialty_id)
    
    context = {
        'students': students,
        'chairs': chairs,
        'chair_id': chair_id,
    }
    return render(request, 'students.html', context)




