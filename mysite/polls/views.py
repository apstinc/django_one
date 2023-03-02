from django.shortcuts import render
from django.http import HttpResponse

def index(reauest) :
    welcom_string = 'Hello APST'
    return HttpResponse(welcom_string)
    
# Create your views here.
