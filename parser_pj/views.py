from django.shortcuts import render, redirect


# Create your views here.
def redirect_view(request):
    response = redirect('/admin/')
    return response