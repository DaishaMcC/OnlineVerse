from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views import View


# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserRegisterView(View):
    template_name = "users/register.html"

    def get (self, request):
        return render(request, self.template_name)