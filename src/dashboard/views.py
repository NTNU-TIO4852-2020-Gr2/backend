from django.shortcuts import render


def dashboard(request):
    context = {}
    return render(request, "dashboard/main.html", context)
