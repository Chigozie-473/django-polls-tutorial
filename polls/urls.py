from django.urls import path
from . import views

app_name = "polls"  # ← this is optional, but if you use it, you need it in your template

urlpatterns = [
    path("", views.index, name="index"),  # e.g., /polls/
    path("<int:question_id>/", views.detail, name="detail"),  # e.g., /polls/2/
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]