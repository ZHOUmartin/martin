import markdown
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from blog.models import Post
import markdown
# Create your views here.
from comments.forms import CommentForm


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',context={
        'post_list':post_list,
        'contacts':contacts,
    })

def detail(request,pk):
    body = get_object_or_404(Post,pk=pk)
    body.body = markdown.markdown(body.body,['extra','codehilite','toc'])
    form = CommentForm()
    comment_list = body.comment_set.all()
    context = {'body':body,
               'form':form,
               'comment_list':comment_list}
    return render(request,'blog/detail.html',context=context)