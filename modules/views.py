from django.shortcuts import render, get_object_or_404
from .models import Review, Contact
from django.contrib.auth.models import User
# from django.views.generic import (
#     ListView,
#     DetailView,
# )


# Create your views here.

def home(request):
    return render(request, 'modules/home.html')


def suggest(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sug = request.POST['suggestions']
        suggestvar = Review(name=name, email=email, sug=sug)
        suggestvar.save()

    return render(request, 'modules/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        comments = request.POST['comments']
        contact = Contact(name=name, email=email, phone=phone, address=address, comments=comments)
        contact.save()

    return render(request, 'modules/contact.html')


def projects(request):
    return render(request, 'modules/projects.html')


def discover(request):
    return render(request, 'modules/discover.html')


# blog


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'modules/blog.html', context)
#
#
# class Bloghome(ListView):
#     model = Post
#     template_name = 'modules/blog.html'
#     context_object_name = 'posts'
#     ordering = ['date_posted']
#     paginate_by = 5

# class PostListView(ListView):
#     model = Post
#     template_name = 'modules/blog.html'
#     context_object_name = 'posts'
#     ordering = ['date_posted']
#     paginate_by = 5

# class BlogList(ListView):
#     model = Post
#     template_name = 'modules/bloglist.html'
#     context_object_name = 'posts'
#     # paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('date_posted')
#
#
# class BlogDetail(DetailView):
#     model = Post
