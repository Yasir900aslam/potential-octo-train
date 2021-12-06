from django.http import JsonResponse
from django.db.models import Prefetch
from .models import HotelRoom, Listing, HotelRoomType, ReservationInfo
from .serializers import HotelRoomSerializer, ListingSerializer, HotelRoomTypeSerializer, ReservationInfoSerializer
from django.shortcuts import get_object_or_404


def get_all_lists(request):
    listing_serializer = ListingSerializer(Listing.objects.all(), many=True)
    return JsonResponse(listing_serializer.data, safe=False)


def get_list_with_id(request, pk):
    list_by_id = get_object_or_404(Listing, pk=pk)
    list_serializer = ListingSerializer(list_by_id, many=False)
    return JsonResponse(list_serializer.data, safe=False)


def get_all_hotel_rooms_type(request):
    queryset = HotelRoomType.objects.select_related('hotel')
    hotel_room_serializer = HotelRoomTypeSerializer(
        queryset, many=True)
    return JsonResponse(hotel_room_serializer.data, safe=False)


def get_hotel_room_type(request, pk):
    queryset = HotelRoomType.objects.select_related("hotel").get(id=pk)
    hotel_room_serializer = HotelRoomTypeSerializer(queryset, many=False)
    return JsonResponse(hotel_room_serializer.data, safe=False)


def get_hotel_rooms(request):
    queryset = HotelRoom.objects.prefetch_related(
        'hotel_room_type__hotel').all()
    hotel_room_serializer = HotelRoomSerializer(queryset, many=True)
    return JsonResponse(hotel_room_serializer.data, safe=False)


def get_specific_hotel_room(request, pk):
    queryset = HotelRoom.objects.select_related(
        "hotel_room_type__hotel").get(id=pk)
    hotel_room_serializer = HotelRoomSerializer(queryset, many=False)
    return JsonResponse(hotel_room_serializer.data, safe=False)


def get_all_reservations(request):
    queryset = ReservationInfo.objects.select_related(
        'booking__listing').all()
    reservation_serializer = ReservationInfoSerializer(queryset, many=True)
    return JsonResponse(reservation_serializer.data, safe=False)


def get_specific_reservation(request, pk):
    queryset = ReservationInfo.objects.prefetch_related(
        "booking__listing").get(id=pk)
    reservation_serializer = ReservationInfoSerializer(queryset, many=False)
    return JsonResponse(reservation_serializer.data, safe=False)


def get_reservation_by_filters(request, pk):
    None
