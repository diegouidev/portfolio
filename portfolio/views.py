from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project


def index(request):
    category = request.GET.get('category', '')
    if category in ('design', 'web'):
        projects = Project.objects.filter(category=category)
    else:
        projects = Project.objects.all()
        category = ''

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'current_category': category,
    })


def contact(request):
    if request.method != 'POST':
        return redirect('portfolio:index')

    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip() or 'Contato via Portfólio'
    message = request.POST.get('message', '').strip()

    if name and email and message:
        try:
            send_mail(
                subject=f'[Portfólio] {subject}',
                message=f'De: {name} <{email}>\n\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@portfolio.local',
                recipient_list=[settings.CONTACT_EMAIL] if hasattr(settings, 'CONTACT_EMAIL') else [],
                fail_silently=True,
            )
        except Exception:
            pass

    category = request.GET.get('category', '')
    projects = Project.objects.filter(category=category) if category in ('design', 'web') else Project.objects.all()

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'current_category': category,
        'contact_success': True,
    })
