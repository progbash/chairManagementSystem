from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Chair, Specialty, Degree, Specialization, Teacher, Subject, Article, Language, CGroup, Student

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'post_date', 'image')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'specialty', 'group', 'course')

admin.site.site_header = "AzTU - Kafedra Avtomatlaşdırılmış İnformasiya Sistemi" 
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Chair)
admin.site.register(Specialty) 
admin.site.register(Degree) 
admin.site.register(Specialization)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Language)
admin.site.register(CGroup)
admin.site.register(Student, StudentAdmin)
admin.site.register(Article, ArticleAdmin)
