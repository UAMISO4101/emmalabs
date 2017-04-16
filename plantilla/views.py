from django.shortcuts import render

from usuario.models import LoginForm


# Create your views here.

def index(request):
    form_login = LoginForm()
    context = {'form_login': form_login, }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')
