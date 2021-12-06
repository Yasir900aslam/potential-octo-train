from django.urls import path

from .views import get_all_lists, get_list_with_id, get_all_hotel_rooms_type, get_hotel_room_type, get_hotel_rooms, get_specific_hotel_room, get_all_reservations, get_specific_reservation, get_reservation_by_filters

urlpatterns = [
    path('lists/', get_all_lists),
    path('lists/<int:pk>', get_list_with_id),
    path('hotel_room_types/', get_all_hotel_rooms_type),
    path('hotel_room_types/<int:pk>', get_hotel_room_type),
    path('hotel_rooms/', get_hotel_rooms),
    path('hotel_rooms/<int:pk>', get_specific_hotel_room),
    path('reservations/', get_all_reservations),
    path('reservations/filters',
         get_reservation_by_filters),
    path('reservations/<int:pk>', get_specific_reservation),
    # http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12

]
