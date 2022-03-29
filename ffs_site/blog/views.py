from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from .models import FFDiary
from django.contrib.auth.models import User


def index(request):
    return render(request, 'blog/base.html')

def timeline_view(request, username):
    post_form = PostForm()
    user = get_object_or_404(User, username=username)
    posts = FFDiary.objects.filter(user=user).order_by('-create_at')
    return render(request, 'blog/timeline.html', {'posts':posts, 'post_form':post_form})

@login_required
@require_POST
def add_view(request):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = request.user
        post.time = datetime.today().strftime('%H')
        post.save()
    return HttpResponseRedirect(reverse('blog:timeline', kwargs={'username': request.user.username}))
