from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Login(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):    
        if request.user.is_authenticated:
            return Response({'detail': 'login success'} , status=status.HTTP_200_OK)
        username = request.data.get('username')
        password = request.data.get('password')
        _user = authenticate(request, username=username, password=password)
        if _user is not None:
            login(request, _user)
            return Response({'detail': 'login success'}, status=status.HTTP_200_OK)
        return Response({"detail":"login failed"}, status=status.HTTP_400_BAD_REQUEST)