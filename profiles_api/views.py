from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


# Create your views here.
class HelloAPIView(APIView):
    """Test APIView."""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
        'a',
        'b',
        'c',
        'd',
        'e'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handling a partial object"""
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        """Deleting an object"""
        return Response({'method':'DELETE'})



# for testing purpose
# class Dhanush(APIView):
#     """testing"""
#     def get(self,request,format=None):
#         a="apple"
#         return  Response({'message':'test','a':a})
