from django.urls import reverse_lazy
from django.views import generic

from .forms import SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

