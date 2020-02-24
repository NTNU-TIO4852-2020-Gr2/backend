from django.shortcuts import render


def home(request):
    context = {}
    context["breadcrumblist"] = [
        ("Home", "/"),
    ]
    return render(request, "home.html", context)
