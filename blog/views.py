
# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
# from .forms import CommentForm # later for comments

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-publish')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(approved=True)
    # new_comment = None
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = post
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        # 'comment_form': comment_form,
        # 'new_comment': new_comment,
    })