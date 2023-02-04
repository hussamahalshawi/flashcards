from django.urls import path
# from django.views.generic import TemplateView
from . import views

# urlpatterns = [
#     path("", TemplateView.as_view(template_name="cards/base.html"),name="home")
# ]
urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
        ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
        ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
        ),
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
        ),
]