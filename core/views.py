from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def index_paper(request):
    return render(request, 'index_p.html')
