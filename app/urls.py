from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('solutions/', views.solutions_view, name="solutions"),
    path('signup/', views.signup_view, name="signup"),
]
