from django.urls import path

from .views import get_all_lists, get_list_with_id

urlpatterns = [
    path('lists/', get_all_lists),
    path('lists/<int:pk>', get_list_with_id)
]
