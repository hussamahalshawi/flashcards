from django.urls import path
# from django.views.generic import TemplateView
from . import views

# urlpatterns = [
#     path("", TemplateView.as_view(template_name="cards/base.html"),name="home")
# ]
urlpatterns = [
    path("",views.CardListView.as_view(),name="card-list"),
]