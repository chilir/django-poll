# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("asdf;lakjsdf;laskjdf;lkajsd;fljk;alskdfj")
