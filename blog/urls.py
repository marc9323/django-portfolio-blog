from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # int after path blog saved as ...
    path('<int:blog_id>/', views.detail, name='detail')
]