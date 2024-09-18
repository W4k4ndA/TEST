from django.urls import path
from . import views


app_name = 'Blog'


urlpatterns = [
    path('', views.BlogList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view()),
    path('search/<str:term>/', views.BlogSearchView.as_view()),
]
