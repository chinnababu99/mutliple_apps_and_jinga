from django.shortcuts import render

# Create your views here.
def user1 (request):
    d={'name':'chinna babu'}
    return render(request,'user1.html',d)

def user2 (request):
    d={'name':'Madhura'}
    return render(request,'user2.html',d)