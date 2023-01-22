from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post, SocialUser, Comment, User
from django.urls import reverse_lazy, reverse
from itertools import chain
from operator import attrgetter
from .forms import CommentForm
import re

class TimelineView(ListView):

    model = Post
    template_name = "timeline.html"
    context_object_name = "all_relevant_posts"

    def get_queryset(self):
        # This is where I fetch/filter all relevant posts, so once I add friends and such the code for filtering probably will go here
        followed_users = SocialUser.objects.get(
            user=self.request.user).following
        posts = []
        current_users_posts = Post.objects.filter(author=self.request.user.id)
        posts.append(current_users_posts)

        if not followed_users == None:
            for user in followed_users:
                this_users_id = User.objects.get(username=user).id
                this_users_posts = Post.objects.filter(author=this_users_id)
                posts.append(this_users_posts)

        posts_to_return = sorted(
            list(chain(*posts)), key=attrgetter('created'), reverse=True)
        return posts_to_return


class LandingView(View):

    def get(self, request):
        return render(request, "landing.html")


class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all
        if post.likes.filter(id=request.user.id).exists():
            liked = True
        else:
            liked = False

        return render(request,
                      "post-details.html",
                      {
                          "post": post,
                          "comments": comments,
                          "comment_form": CommentForm(),
                          "liked" : liked,
                      })

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request,
                      "post-details.html",
                      {
                          "post": post,
                          "comments": comments,
                          "comment_form": CommentForm()
                      })


class AddPostView(CreateView):

    model = Post
    template_name = "add_post.html"
    fields = 'title', 'content', 'images'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        extracted_urls = re.search('images" value="(.*)" id="id_', str(form))
        try: 
            extracted_urls_array = extracted_urls.group(1).split(' ')
        except AttributeError:
            extracted_urls_array = []
        # Ensure there are no empty items:
        for item in extracted_urls_array:
            if (item == "") or (item == " ") or (item == "deleted"):
                extracted_urls_array.remove(item)
        form.instance.images = extracted_urls_array
        return super(AddPostView, self).form_valid(form)


class UpdatePostView(UpdateView):

    model = Post
    template_name = "update_post.html"
    fields = 'title', 'content', 'images'

    def form_valid(self, form):
        extracted_urls = re.search('images" value="(.*)" id="id_', str(form))
        try: 
            extracted_urls_array = extracted_urls.group(1).split(' ')
        except AttributeError:
            extracted_urls_array = []
        # Ensure there are no empty items:
        for item in extracted_urls_array:
            if (item == "") or (item == " ") or (item == "deleted"):
                extracted_urls_array.remove(item)
        form.instance.images = extracted_urls_array
        return super(UpdateView, self).form_valid(form)


class DeletePostView(DeleteView):

    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("timeline")


class ProfileView(View):

    def get(self, request, viewed_user_id):
        viewed_user = SocialUser.objects.get(user=viewed_user_id)
        return render(request, "profile.html", {
            "viewed_user": viewed_user,
            "viewed_user_posts": Post.objects.filter(author=viewed_user_id)
        })
    


class EditProfileView(UpdateView):

    model = SocialUser
    template_name = "edit_profile.html"
    fields = 'bio', 'location', 'age', 'profile_image',


class EditCommentView(UpdateView):

    model = Comment
    template_name = "edit-comment.html"
    fields = ('body',)


class CircleView(ListView):

    model = SocialUser
    template_name = 'circle.html'
    context_object_name = "social_users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followed_users = SocialUser.objects.get(
            user=self.request.user).following
        context["followed_users"] = followed_users
        return context


class UserListView(ListView):

    model = SocialUser
    template_name = "user_list.html"
    context_object_name = "social_users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followed_users = SocialUser.objects.get(
            user=self.request.user).following
        context["followed_users"] = followed_users
        return context


class FollowUserView(View):

    def post(self, request, user_to_follow, *args, **kwargs):
        followed_users = SocialUser.objects.get(user=self.request.user)
        if followed_users.following == None:
            followed_users.following = [user_to_follow]
        else:
            if user_to_follow not in followed_users.following:
                followed_users.following.append(user_to_follow)
        followed_users.save()
        return redirect('circle')


class UnfollowUserView(View):

    def post(self, request, user_to_unfollow, *args, **kwargs):
        followed_users = SocialUser.objects.get(user=self.request.user)
        if not followed_users.following == None:
            followed_users.following.remove(user_to_unfollow)
        followed_users.save()
        return redirect('circle')

class LikePostView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-details', args=[slug]))