from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'test.html')

def department(request):
    return render(request, 'department.html')

def table(request):
    return render(request, 'table.html')

def gal(request):
    return render(request, 'gal.html')

def gal2(request):
    return render(request, 'gal2.html')

def gal3(request):
    return render(request, 'gal3.html')

def base(request):
    return render(request, 'base.html')