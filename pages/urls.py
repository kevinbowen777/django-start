from django.urls import path

from .views import AboutPageView, HomePageView, SamplePageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("sample1/", SamplePageView.as_view(), name="sample"),
    path("", HomePageView.as_view(), name="home"),
]
