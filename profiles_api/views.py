from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloAPIView(APIView):
    """Test APIView."""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
        'a',
        'b',
        'c',
        'd'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
