from django.shortcuts import render

posts = [
    {
        'author': 'Ryn',
        'title': 'Dummy Post',
        'content': 'This is a Dummy Post',
        'date_posted': '7/15/2020',
        'category' : "Dummy",
        "comment_count" : 25
    }
]

def index(request):
    context = {
            'posts': posts
        }
    return render(request, 'index.html', context)


def about(request):
     return render(request, 'about.html', {'title': 'About'})
    
def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')