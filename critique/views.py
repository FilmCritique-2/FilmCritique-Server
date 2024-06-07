from django.shortcuts import render, get_object_or_404
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Review
# Create your views here.

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@api_view(['POST'])
def validate_password(request, pk):
    review = get_object_or_404(Review, pk=pk)

    password = request.data['password']

    if password == review.password:
        return Response({"password": True})
    
    return Response({"password": False})