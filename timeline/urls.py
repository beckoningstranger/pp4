from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('timeline/', views.TimelineView.as_view(), name="timeline"),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name="post-details"),
    path('add-post/', views.AddPostView.as_view(), name="add-post"),
    path('update-post/<slug:slug>', views.UpdatePostView.as_view(), name="update-post"),
    path('delete-post/<slug:slug>', views.DeletePostView.as_view(), name="delete-post"),
    path('user-list/', views.UserListView.as_view(), name="user-list"),
    path('profile/<int:viewed_user_id>', views.ProfileView.as_view(), name="profile"),
    path('profile/edit/<int:pk>', views.EditProfileView.as_view(), name="edit-profile"),
    path('mycircle', views.CircleView.as_view(), name="circle"),
    path('edit-comment/<int:pk>', views.EditCommentView.as_view(), name="edit-comment"),
    path('follow-user/<str:user_to_follow>', views.FollowUserView.as_view(), name="follow-user"),
    path('unfollow-user/<str:user_to_unfollow>', views.UnfollowUserView.as_view(), name="unfollow-user"),
    path('like-post/<slug:slug>', views.LikePostView.as_view(), name="like-post"),
]
