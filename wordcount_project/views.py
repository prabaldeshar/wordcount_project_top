from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse("I like egges")

worddict = {}

def count(request):
    fulltext = request.GET['fulltext']
    list = fulltext.split()
    print(list)
    count = len(list)
    for word in list:
        if word in worddict:
            worddict[word] =worddict[word]+1
        else:
            worddict[word] = 1
    return render(request, 'count.html',{'fulltext':fulltext, 'count': count, 'worddict':worddict.items()})

def split(request):
    text = request.GET['newtext']
    split_text = text.split()

    return render(request, 'split.html', {'split_text':split_text, 'full_text':text})

def about(request):
    return render(request, 'about.html')
