from django.db import models
from tinymce.models import HTMLField
from django_countries.fields import CountryField

class Chair(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    chairman = models.CharField(max_length=30)

class Degree(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)
        
class Specialty(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    specialty_code = models.IntegerField(null=True)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

class Specialization(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

class Subject(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    credit = models.IntegerField()

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    academic_degree = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
    image = models.CharField(max_length=2000)
    citizenship = CountryField()
    language = models.ManyToManyField(Language)


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    content = HTMLField()
    image = models.CharField(max_length=2000)
    # image = models.ImageField(upload_to='media')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CGroup(models.Model):
    name = models.CharField(max_length=15)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    ed_year = models.CharField(max_length=9)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_year = models.DateField()
    score = models.IntegerField()
    gpa = models.IntegerField()
    course = models.CharField(max_length=2)
    group = models.ForeignKey(CGroup, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name