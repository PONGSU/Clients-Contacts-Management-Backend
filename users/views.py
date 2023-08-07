from rest_framework import generics
from .models import User
from .serializers import NormalUserSerializer, AdminManageUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner, IsAdminUser, IsAccountOwnerOrAdminUser


# Create your views here.
class NormalUserView(generics.CreateAPIView):
    """
    Registro de usuários
    """

    queryset = User.objects.all()
    serializer_class = NormalUserSerializer


class AdminUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = AdminManageUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdminUser]

    queryset = User.objects.all()
    serializer_class = NormalUserSerializer
