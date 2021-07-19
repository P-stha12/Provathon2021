from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
from bs4 import BeautifulSoup

# Create your views here.

def covid_datas():
    req = requests.get('https://covid19.ekantipur.com')
    soup = BeautifulSoup(req.content, 'lxml')
    datas = {}
    tadas = soup.find_all('span', {'class':'nepal-total'})[0]
    tadas = tadas.find_all('div')
    datas['infected']= tadas[0].find('span').text
    datas['active_cases'] = tadas[1].find('span').text
    datas['deaths']= tadas[2].find('span').text
    datas['recovered'] = tadas[3].find('span').text
    return datas

def home_view(request):
    posts = Post.objects.all()
    #covid_data = covid_datas()
    return render(request, 'posts/index.html', {'posts': posts})

def contact_view(request):
    return render(request, 'posts/contact_us.html')

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    template_name = 'posts/ask_question.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def covid_view(request):
    return render(request, 'posts/covid_center.html')

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/index.html'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/single_question.html'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'settled']
    template_name = 'posts/ask_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
