# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render
import os
import re

# def index(request):
#     return HttpResponse("<h1>hello Jeet</h1>")

def about(request):
    return HttpResponse("Congratulations Jeet")

# def index(request):
#     a = open('textutils/one.txt','r+')
#     return HttpResponse(a.read())

# def index(request):
#     return HttpResponse('''<a href ="https://www.youtube.com"> Youtube </a>''')


def index(request):
    params = {'name': 'Jeet', 'place': 'Stars'}
    return render(request,'index.html',params)
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Chaeck checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    #chech with checkbox is on
    if removepunc == "on":
        punctuations =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request,'analyze.html',params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if (spaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if (charcount == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose':'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request,'analyze.html',params)

# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def spaceremove(request):
#     return HttpResponse("Space Remove <a href ='/'>back</a>")



