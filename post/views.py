from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Count



# Create your views here.



def blog_view(request):
    qs = Post.objects.all().order_by('-published')
    paginator = Paginator(qs, 10)  # Show 10 contacts per page.

    page_number = request.GET.get("page")
    qs = paginator.get_page(page_number)
    context = {'post':qs}
    return render(request,'blog/post_list.html',context)

def detail_view(request, slug=None):
    qs = get_object_or_404(Post, slug=slug)
    context = {"blog": qs}
    return render(request,'blog/post_detail.html',context)    




