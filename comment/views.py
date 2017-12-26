from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post
from comment.forms import CommentForm


def post_comment(request,post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        t = request.POST
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            return redirect(post,form.errors)

    return redirect(post)