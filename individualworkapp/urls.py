from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chairs', views.chairs, name='chairs'),
    path('articles', views.articles, name='articles'),
    path('chairs/<int:chair_id>', views.list_of_specialties, name='list_of_specialties'),
    path('chairs/<int:chair_id>/<int:specialty_id>', views.list_of_specializations, name='list_of_specializations'),
    path('chairs/<int:chair_id>/teachers', views.list_of_teachers, name='list_of_teachers'),
    path('article/<int:article_id>', views.article, name='article'),
    path('chairs/<int:chair_id>/<int:specialty_id>/groups', views.list_of_groups, name='list_of_groups'),
    path('chairs/<int:chair_id>/<int:specialty_id>/students', views.list_of_students, name='list_of_students')
]