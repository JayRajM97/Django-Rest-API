from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#This is NOT the package, but file from the same root folder
from . import serializers


# Create your views here.

class HelloApiView(APIView):
    """Test APIView (HelloApiView)"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retuens a list of APIView Features"""

        an_apiview = [
            'Tony Stark',
            'Dr. Stephen Strange',
            'Thor'
        ]

        return Response({'message': 'Avengers', 'an_apiview': an_apiview})

        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else :
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handels updating an object"""
        return Response({'method': 'put'})

    def post(self, request, pk=None):
        """Handels updating an object"""
        return Response({'method': 'post'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    #List Object: Lists all the object used in the function
    def list(self, request):
        """Return Hello Message"""

        a_viewset = [
            'Friday',
            'Yong',
            'Stormbreaker'
        ]

        return Response({'message': "Hello!", 'a_viewset': a_viewset})

    def create(self, request):
        '''Create a new hello message'''

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST
            )
        def retrieve(self, request, pk=None):
            """Handels getting an object by it's ID"""

            return Response({'http_method' : 'GET'})

        def update(self, request, pk=None):
            """Handels updating an object"""

            return Response({'http_method' : 'PUT'})

        def partial_update(self, request, pk=None):
            """Handels updating a part of the object"""

            return Response({'http_method' : 'PATCH'})

        def destroy(self, request, pk=None):
            """Handels getting an object by it's ID"""

            return Response({'http_method' : 'DELETE'})
