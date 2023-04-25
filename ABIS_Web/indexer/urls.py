from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('indexer/import-page', views.import_page, name='import'),
   path('indexer/about', views.about, name='about')
]
