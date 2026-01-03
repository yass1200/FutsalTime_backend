from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

def home(request):
    # Simple landing page ("design") to make the project presentable
    return render(request, "web/home.html")

def api_root(request):
    return JsonResponse({
        "auth": "/api/auth/",
        "fields": "/api/fields/",
        "reservations": "/api/reservations/",
        "notifications": "/api/notifications/",
        "schema": "/api/schema/",
        "docs": "/api/docs/",
    })
