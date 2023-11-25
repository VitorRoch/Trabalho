from django.urls import path
from portfolio.views import home, trama, imagens, atores

urlpatterns = [
    path('', home),
    path('trama/', trama),
    path('imagens/', imagens),
    path('atores/', atores),
]





