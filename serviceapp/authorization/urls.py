from django.urls import path

from serviceapp.authorization.views import profile_view

urlpatterns = [
    path('profile/', profile_view, name="profile"),
]