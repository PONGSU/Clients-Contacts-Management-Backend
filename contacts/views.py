from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status




class ContactListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @extend_schema(
        operation_id="get_contacts",
        description="Rota para listagem de todos os contatos registrados. Aceita parâmetro opcional de paginação ex: .../api/contacts/?page=2/. Requer autenticação de admin.",
        summary="Listar todos os contatos",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContactCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @extend_schema(
        operation_id="post_contact",
        description="Rota para registro de um contato. Usuário precisa estar logado.",
        summary="Cadastrar um contato",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['user'] = request.user
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdminUser]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @extend_schema(
        operation_id="get_id_contact",
        description="Rota de listagem de um contato. Requer autenticação do cliente associado ou um administrador.",
        summary="Listar um contato",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(operation_id="put_id_contact", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="patch_id_contact",
        description="Rota de atualização de um contato. Requer autenticação do cliente associado ou um administrador.",
        summary="Atualizar contato",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="delete_id_contact",
        description="Rota de deleção de um contato. Requer autenticação do cliente associado ou um administrador.",
        summary="Deletar Contato",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
