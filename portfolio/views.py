from django.shortcuts import render
from .models import Project


def index(request):
    """Página principal do portfólio."""
    category = request.GET.get('category', '')

    if category in ('design', 'web'):
        projects = Project.objects.filter(category=category)
    else:
        projects = Project.objects.all()
        category = ''

    context = {
        'projects': projects,
        'current_category': category,
    }
    return render(request, 'portfolio/index.html', context)
