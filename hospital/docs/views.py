from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import DocsForm
from .models import Docs

# Create your views here.
def main_view(request):
    return HttpResponse("<h1>Hello Django</h1>")

def setcookie(request):
    html = HttpResponse("<h1>Hello Pragati</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie("Pragati",'Welcome back cookie')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits',value+1)
    else:
        value =1
        text = "Hello this is your first cookie"
        html.set_cookie('visits',value)
        html.set_cookie('Pragati',text)
    return html

def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('Pragati')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text,value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect(reverse('docs:setcookie'))

def deletecookie(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>Pragati<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>Pragati</h1>need to create cookie before deleting")
    return response

def custom_view(request):
#     return render(request,'docs.html')
#this is to download image from our site.
    docs=get_object_or_404(Docs,pk=3)
    context = {
        'docs':docs
    }
    return render(request,'docs/docs.html',context)

def Static_view(request):
    return render(request,"docs/static_demo.html")

def Docs_create_view(request):
    form = DocsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    form = DocsForm
    context = {
        'form':form
    }
    return render(request,'docs/docs_create.html',context)

def Docs_update_view(request,pk):
    docs=get_object_or_404(Docs,pk=pk)
    form = DocsForm(request.POST or None,instance=docs)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'docs/docs_update.html',context)

def Docs_delete_view(request,pk):
    docs = get_object_or_404(Docs,pk=pk)
    if request.method == 'POST':
        docs.delete()
        return redirect(reverse('docs:docs_list_view'))
    context = {
        'docs':docs
    }
    return render(request,'docs/docs_delete.html',context)

def Docs_list_view(request):
    docs = Docs.objects.all()
    context = {
        'docs':docs
    }
    return render(request,'docs/docs_list.html',context)

def Docs_detail_view(request,pk):
    docs = get_object_or_404(Docs,pk=pk)
    context={
        'docs':docs
    }
    return render(request,'docs/docs_detail.html',context)