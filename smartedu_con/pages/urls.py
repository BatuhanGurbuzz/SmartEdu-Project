from django.urls import path
from .views import AboutViews, IndexViews, ContactViews

urlpatterns = [
    path('', IndexViews.as_view(), name="index"),
    path('about/', AboutViews.as_view(), name="about"),
    path('contact/', ContactViews.as_view(), name="contact"),
]
