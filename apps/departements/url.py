from django.urls import path
from .views import git,gem,gc,tc


urlpatterns = [
    path("git/",git,name="git"),
    path("gem/",gem,name="gem"),
    path("gc/",gc,name="gc"),
    path("tc/",tc,name="tc")
]