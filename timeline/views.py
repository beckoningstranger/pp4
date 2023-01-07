from django.shortcuts import render
from django.views import View

class TimelineView(View):

    def get(self, request):
        return render(request, "timeline.html")

class LandingView(View):

    def get(self, request):
        return render(request, "landing.html")
