from django.urls import path
from .views import create_project, my_projects, project_detail

urlpatterns = [

    path('create/', create_project, name='create_project'),
    path('my-projects/', my_projects, name='my_projects'),
    path('detail/<int:id>/', project_detail, name='project_detail'),

]