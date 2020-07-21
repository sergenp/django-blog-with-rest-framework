from django.shortcuts import render

posts = [
    {
        'author': 'Ryn',
        'title': 'Dummy Post',
        'content': 'This is a Dummy Post',
        'date_posted': '7/15/2020'
    }
]

def home(request):
    context = {
            'posts': posts
        }
    return render(request, 'home.html', context)


def about(request):
     return render(request, 'about.html', {'title': 'About'})
