from django.urls import path
from .views import ( 
    UpdateView, 
    DetailView, 
    DeleteView, 
    CreateView,
    )

urlpatterns = [
    path('<int:pk>/edit/', UpdateView.as_view(), name='edit'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('new/', CreateView.as_view(), name='new'),
]