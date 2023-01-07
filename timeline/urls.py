from django.urls import path
from . import views

urlpatterns = [
    path('timeline/', views.TimelineView.as_view(), name="timeline"),
    path('', views.LandingView.as_view(), name="landing"),
]
