from django.urls import path

from .views import (
    AboutPageView,
    ContactView,
    HomePageView,
    SampleView,
    SuccessView,
)

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactView, name="contact"),
    path("success/", SuccessView, name="success"),
    path("sample/", SampleView, name="sample"),
    path("", HomePageView.as_view(), name="home"),
]
