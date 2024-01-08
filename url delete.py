from django.urls import path
from .views import delete_item

urlpatterns = [
    path('delete/<int:pk>/', delete_item, name='delete_item'),
    # ... other patterns
]
