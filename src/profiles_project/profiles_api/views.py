from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test APIView (HelloApiView)"""

    def get(self, request, format=None):
        """Retuens a list of APIView Features"""

        an_apiview = [
            'Tony Stark',
            'Dr. Stephen Strange',
            'Thor'
        ]

        return Response({'message': 'Avengers', 'an_apiview': an_apiview})
