from django.shortcuts import render

# Create your views here.
from django.views.generic import (ListView,) 
from .models import Card
class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")