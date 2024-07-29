from django.urls import path

from . import views

app_name = 'reina'

urlpatterns = [
    path('', views.SituationListView.as_view(), name='situation-list'),
    path('add/', views.SituationCreateView.as_view(), name='situation-create'),

]
