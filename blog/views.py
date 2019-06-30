from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def hello_irina(request):
    return render(request, 'blog/irina.html', {})

def hello_adrian(request):
    return render(request, 'blog/adrian.html', {})