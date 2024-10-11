from django.urls import path
from . import views

urlpatterns = [
    path('a11y-list/', views.A11yListView, name='a11y-list'),
    path('page-details/<path:url>/', views.PageDetailsView, name='page-details'),
]
