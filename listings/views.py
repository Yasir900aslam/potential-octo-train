from django.http import JsonResponse
from .models import Listing
from .serializers import ListingSerializer
from django.shortcuts import get_object_or_404


def get_all_lists(request):
    listing_serializer = ListingSerializer(Listing.objects.all(), many=True)
    return JsonResponse(listing_serializer.data, safe=False)


def get_list_with_id(request, pk):
    list_by_id = get_object_or_404(Listing, pk=pk)
    list_serializer = ListingSerializer(list_by_id, many=False)
    return JsonResponse(list_serializer.data, safe=False)
