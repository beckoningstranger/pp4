from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from .models import Post


class TimelineView(ListView):

    model = Post
    template_name = "timeline.html"
    context_object_name = "all_relevant_posts"

    def get_queryset(self):
        # This is where I fetch/filter all relevant posts, so once I add friends and such the code for filtering probably will go here
        return Post.objects.filter(author=self.request.user.id)


class LandingView(View):

    def get(self, request):
        return render(request, "landing.html")


class PostDetailView(DetailView):

    model = Post
    template_name = "post-details.html"


class AddPostView(CreateView):

    model = Post
    template_name = "add_post.html"
    # fields = 'title', 'content'
    fields = 'title', 'content'
