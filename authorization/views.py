from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import TeacherLoginSerializer


class TeacherLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeacherLoginSerializer(data=request.data)
        if serializer.is_valid():
            usertag = serializer.validated_data['usertag']
            password = serializer.validated_data['password']
            User = get_user_model()
            try:
                user = User.objects.get(usertag=usertag)
                if user.check_password(password):
                    if user.is_active:
                        refresh = RefreshToken.for_user(user)
                        return Response({
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                        })
                    else:
                        return Response({'error': 'Account disabled.'}, status=status.HTTP_403_FORBIDDEN)
                else:
                    return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error': 'Invalid usertag.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
