from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def myfunctionCall(request):
    return HttpResponse("Hello, this is the homepage.")

def myFunctionAbout(request):
    return HttpResponse("Hello, this is the About Page.")

def myFunctionAdd(request,a,b):
    return HttpResponse("Hello, this is the Add Page."+str(a)+str(b))
def myFunctionJson(request,name,age):
    mydict={
        "name":name,
        "age":age
    }

    return JsonResponse(mydict)

def myFirstPage(request):
    return render(request,'index.html')

def mySecondPage(request):
    return render(request,'second.html')

