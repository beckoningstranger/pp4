from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name="landing"),
    path('timeline/', views.TimelineView.as_view(), name="timeline"),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name="post-details"),
    path('add-post/', views.AddPostView.as_view(), name="add-post"),
]
