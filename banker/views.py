from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from banker.forms import CustomUserCreationForm


class DashboardView(TemplateView):
    template_name = "banker/dashboard.html"


class UserRegistrationView(TemplateView):
    def get(self, request):
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return render(
                request, "registration/register.html",
                {"form": CustomUserCreationForm}
            )
