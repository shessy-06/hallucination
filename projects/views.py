from django.shortcuts import render, redirect
from .models import Project


def create_project(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        budget = request.POST.get('budget')
        deadline = request.POST.get('deadline')

        Project.objects.create(
            client=request.user,
            title=title,
            description=description,
            budget=budget,
            deadline=deadline,
            project_file=request.FILES.get('project_file'),
        )

        return redirect('/')

    return render(request, 'projects/create_project.html')

def my_projects(request):

    projects = Project.objects.filter(
        client=request.user
    )

    context = {
        'projects': projects
    }

    return render(
        request,
        'projects/my_projects.html',
        context
    )


def project_detail(request, id):

    project = Project.objects.get(id=id)

    context = {
        'project': project
    }

    return render(
        request,
        'projects/project_detail.html',
        context
    )