from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def djangos(request):
    return render(request,"Django.html")
def contact(request):
    return render(request,"Contact.html")
def analyzes(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get("removepunc","off")
    fullcaps=request.POST.get("fullcaps","off")
    newlineremover=request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("spaceremover","off")
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Filtered Text', 'analyzed_text': analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Filtered Text', 'analyzed_text': analyzed}
        djtext=analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Filtered Text', 'analyzed_text': analyzed}
        djtext=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Filtered Text', 'analyzed_text': analyzed}
        djtext=analyzed       
    elif removepunc=="off" and fullcaps=="off" and extraspaceremover=="off" and newlineremover=="off":
        return HttpResponse("Please select any operation and try again!")
    return render(request, 'analyze.html', params)

