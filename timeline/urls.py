from django.urls import path
from . import views
from allauth.account.views import LoginView, SignupView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('login', LoginView.as_view(), name="login"),
    path('signup', SignupView.as_view(), name="signup"),
    path('timeline/', login_required(views.TimelineView.as_view()), name="timeline"),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name="post-details"),
    path('add-post/', login_required(views.AddPostView.as_view()), name="add-post"),
    path('update-post/<slug:slug>',
         login_required(views.UpdatePostView.as_view()), name="update-post"),
    path('delete-post/<slug:slug>',
         login_required(views.DeletePostView.as_view()), name="delete-post"),
    path('user-list/', login_required(views.UserListView.as_view()), name="user-list"),
    path('profile/<int:viewed_user_id>',
         views.ProfileView.as_view(), name="profile"),
    path('profile/edit/<int:pk>',
         login_required(views.EditProfileView.as_view()), name="edit-profile"),
    path('mycircle', login_required(views.CircleView.as_view()), name="circle"),
    path('edit-comment/<int:pk>',
         login_required(views.EditCommentView.as_view()), name="edit-comment"),
    path('delete-comment/<int:pk>',
         login_required(views.DeleteCommentView.as_view()), name="delete-comment"),
    path('follow-user/<str:user_to_follow>',
         login_required(views.FollowUserView.as_view()), name="follow-user"),
    path('unfollow-user/<str:user_to_unfollow>',
         login_required(views.UnfollowUserView.as_view()), name="unfollow-user"),
    path('like-post/<slug:slug>',
         login_required(views.LikePostView.as_view()), name="like-post"),
]
handler404 = "timeline.views.page_not_found_view"
