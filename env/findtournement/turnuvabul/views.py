from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request, 'hakkimizda.html')
def turnuvaolustur(request):
    return render(request, 'turnuvaolustur.html')
