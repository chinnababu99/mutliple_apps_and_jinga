from django.shortcuts import render

# Create your views here.
def user3 (request):
    d={'name':'bhaskar'}
    return render (request,'user3.html',d)

def user4 (request):
    d={'name':'savitha'}
    return render (request,'user4.html',d)

