from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

from .serializers import UserSerializer
from .models import CustomUser

@api_view(["POST"])
def sign_up(request):
    if request.method == 'POST':
        serializer = UserSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def sign_in(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None

        if '@' in username:
            try:
                user = CustomUser.objects.get(
                    email=username
                )
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username,
                                password=password)
            
        if user:
            token, _ = Token.objects.get_or_create(
                user=user
            )
            return Response({'token': token.key},
                            status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credatials'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sign_out(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)  