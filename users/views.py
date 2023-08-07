from rest_framework import generics
from .models import User
from .serializers import NormalUserSerializer, AdminManageUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminUser, IsAccountOwnerOrAdminUser
from drf_spectacular.utils import extend_schema


# Create your views here.
class NormalUserView(generics.CreateAPIView):
    """
    Registro de usuários
    """
    queryset = User.objects.all()
    serializer_class = NormalUserSerializer

    @extend_schema(
        operation_id="users_post",
        description="Rota de criação de usuário. Não requer autenticação.",
        summary="Criar usuário",
    )
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AdminUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = AdminManageUserSerializer

    @extend_schema(
        operation_id="users_post_admin",
        description="Rota de criação de usuário administrador. Requer autenticação de administrador.",
        summary="Criar usuário administrador",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdminUser]

    queryset = User.objects.all()
    serializer_class = NormalUserSerializer

    @extend_schema(
        operation_id="users_get_id",
        description="Rota de listagem de usuário. Requer autenticação do próprio usuário ou um administrador.",
        summary="Listar usuário",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(operation_id="users_put_id", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_patch_id",
        description="Rota de atualização de usuário. Requer autenticação do próprio usuário ou um administrador.",
        summary="Atualizar usuário",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_delete_id",
        description="Rota de deleção de usuário. Requer autenticação do próprio usuário ou um administrador.",
        summary="Deletar usuário",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
