from .models import Listing, HotelRoomType, HotelRoom, BookingInfo, ReservationInfo
from rest_framework import serializers


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class HotelRoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomType
        fields = "__all__"
        depth = 1


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = '__all__'
        depth = 2


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = '__all__'
        depth = 2


class ReservationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationInfo
        fields = '__all__'
        depth = 3
