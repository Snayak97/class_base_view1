from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import *
#fbv in from of string
def Fbv_string(request):
    return HttpResponse(' this is Fbv_string')


#fbv in from of render
def Fbv_temp(request):
    return render(request,'Fbv_temp.html')


#Cbv in from of string
class CBV_string(View):
    def get(self,request):
        return HttpResponse('#fbv in from of string')
    
#Cbv in from of templates
class CBV_temp(View):
    def get(self,request):
        return render(request,'CBV_temp.html')
    
class CBV_t(TemplateView):
    template_name='CBV_temp.html'



