from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Project, Skill, Service, ContactMessage


def home(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not subject or not message:

            messages.error(
                request,
                "Please fill in all fields."
            )

        else:

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(
                request,
                "Your message has been sent successfully."
            )

            return redirect("home")

    projects = Project.objects.all()

    skills = Skill.objects.all()

    services = Service.objects.all()

    context = {
        "projects": projects,
        "skills": skills,
        "services": services,
    }

    return render(
        request,
        "portfolio/home.html",
        context
    )