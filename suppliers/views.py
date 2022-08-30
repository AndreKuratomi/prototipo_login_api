from django.contrib.auth import authenticate
from django.core.mail import EmailMessage, mail_admins, send_mail
from django.template import loader
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from suppliers.serializers import RegisterSupplierSerializer, LoginSupplierSerializer, AskChangePasswordSerializer, ChangePasswordSerializer

from .models import Supplier

from datetime import datetime, timedelta
import uuid
import ipdb


class RegisterSupplierView(APIView):
    def post(self, request):
        serializer = RegisterSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_supplier = Supplier.objects.filter(email=serializer.validated_data['email']).exists()
        if find_supplier is True:
            return Response({"message": "Fornecedor já registrado!"}, status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        
        # ipdb.set_trace()
        supplier = Supplier.objects.create_user(**serializer.validated_data)
        serializer = RegisterSupplierSerializer(supplier)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        all_suppliers = Supplier.objects.all()
        serializer = RegisterSupplierSerializer(all_suppliers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        # PARA OS ADMINS FUTURAMENTE ACESSAREM AS INF VIA API.


class LoginSupplierView(APIView):
    def post(self, request):
        serializer = LoginSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        # ipdb.set_trace()
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            # .objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AskChangePasswordMailView(APIView):
    def post(self, request):
        serializer = AskChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # VARIÁVEL SENHA PROVISÓRIA:
        reducedUUID = str(uuid.uuid4())[0:8] # E COMO GARANTIR QUE ELA TERÁ UM PRAZO?

        # FORMATAÇÃO DE DATA:
        dia = (timezone.now() - timedelta(hours=3)).strftime("%d/%m/%Y")
        horas = (timezone.now() - timedelta(hours=3)).strftime("%H:%M:%S")

        # PARA OBTER USERNAME PELO EMAIL:
        object = Supplier.objects.get(email=request.data['username'])

        # MUDANÇA SENHAS ATUAL E PROVISÓRIA:
        object.password_provisional = reducedUUID
        object.set_password(str(uuid.uuid4()))
        object.save()

        supplier_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Olá, %s! Recebemos seu pedido por nova senha.</p>
                    <p>Segue abaixo a senha provisória mais o link para alteração de senha:</p>
                    <br>
                    <p>Senha provisória: %s </p>
                    <p>Link para alteração de senha aqui</p>
                    <br>
                    <p>Por favor, não responda este e-mail. Ele é enviado de forma automática.<p>
                    <p>Atenciosamente,</p>
                    <h3>Vestcasa</h3>
                </body>
            </html>
        """ % (object.username, reducedUUID)

        admin_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Notificação: O(A) usuário(a) %s solicitou troca de senha às %s em %s.</p>
                    <p>Segue abaixo a senha provisória mais o link para alteração de senha:</p>
                    <br>
                    <p>Senha provisória de %s: %s </p>
                    <br>
                    
                    <h3>Vestcasa</h3>
                </body>
            </html>
        """ % (object.username, horas, dia, object.username, reducedUUID)

        send_mail(
            "Pedido troca de senha usuário(a) {a1} - Suporte VestCasa".format(a1=object.username),
            "",
            "suporte.troca.senha.teste@gmail.com", 
            [request.data['username']], 
            fail_silently=False,
            html_message=supplier_email_message
            )
        mail_admins(
            "Aviso pedido troca de senha - Usuário(a) {b1}".format(b1=object.username), 
            "",
            fail_silently=False,
            html_message=admin_email_message
            )

        return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)


class ChangePasswordMailView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # FORMATAÇÃO DE DATA:
        dia = (timezone.now() - timedelta(hours=3)).strftime("%d/%m/%Y")
        horas = (timezone.now() - timedelta(hours=3)).strftime("%H:%M:%S")

        # PARA OBTER USERNAME PELA SENHA PROVISÓRIA:
        object2 = Supplier.objects.get(password_provisional=request.data['password_provisional'])

        # DEFINIÇÃO NOVA SENHA:
        object2.set_password(request.data['new_password'])
        object2.save()

        # CONFIRMAÇÃO NOVA SENHA:
        object2.set_password(request.data['repeat_new_password'])
        object2.save()

        supplier_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Olá, %s!</p>
                    <p>Sua senha foi atualizada com sucesso!</p>
                    <br>
                    <p>Siga agora para o login.</p>
                    <br>
                    <p>Por favor, não responda este e-mail. Ele é enviado de forma automática.<p>
                    <p>Atenciosamente,</p>
                    <h3>Vestcasa</h3>
                </body>
            </html>
        """ % (object2.username)

        admin_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Notificação: O(A) usuário(a) %s trocou de senha às %s em %s.</p>
                    <br>
                    <p>Nova senha de %s: %s </p>
                    <br>
                    
                    <h3>Vestcasa</h3>
                </body>
            </html>
        """ % (object2.username, horas, dia, object2.username, request.data['new_password'])

        send_mail(
            "Confirmação troca de senha usuário(a) {a1} - Suporte VestCasa".format(a1=object2.username),
            "",
            "suporte.troca.senha.teste@gmail.com", 
            [object2.email], 
            fail_silently=False,
            html_message=supplier_email_message
            )
        mail_admins(
            "Aviso de troca de senha - Usuário(a) {b1}".format(b1=object2.username), 
            "",
            fail_silently=False,
            html_message=admin_email_message
            )

        return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)

