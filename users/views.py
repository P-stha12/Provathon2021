from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from posts.models import Post
from django.contrib.auth.models import User


def register_user_view(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileForm()
    return render(request, 'users/registration.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def user_profile_view(request):
    return render(request, 'users/user_profile.html')

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'users/user_profile.html'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
