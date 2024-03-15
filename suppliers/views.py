from django.contrib.auth import authenticate
from django.core.mail import EmailMessage, mail_admins, send_mail

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from suppliers.serializers import RegisterSupplierSerializer, LoginSupplierSerializer, LoggedSupplierSerializer, AskChangePasswordSerializer, ChangePasswordSerializer

from .models import Supplier

from datetime import datetime

import uuid
import ipdb


class RegisterSupplierView(APIView):
    def post(self, request):
        serializer = RegisterSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_supplier = Supplier.objects.filter(cnpj=serializer.validated_data['cnpj']).exists()
        if find_supplier is True:
            return Response({"message": "Fornecedor já registrado!"}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        supplier = Supplier.objects.create_user(**serializer.validated_data)
        serializer = RegisterSupplierSerializer(supplier)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        all_suppliers = Supplier.objects.all()
        serializer = RegisterSupplierSerializer(all_suppliers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SupplierByCNPJView(APIView):
    def get(self, request, supplier_cnpj=''):
        try:
            supplier = Supplier.objects.get(cnpj=supplier_cnpj)

            if supplier:
                serialized = RegisterSupplierSerializer(supplier)

                return Response(serialized.data, status=status.HTTP_200_OK)

        except Supplier.DoesNotExist:
            return Response({"message": "Fornecedor não registrado!"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, supplier_cnpj=''):
        serializer = RegisterSupplierSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            updated_supplier = Supplier.objects.filter(cnpj=supplier_cnpj).update(**serializer.validated_data)
            updated = Supplier.objects.get(cnpj=supplier_cnpj)

            serialized = RegisterSupplierSerializer(updated)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except Supplier.DoesNotExist:
            return Response({"message": "Fornecedor não registrado!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, supplier_cnpj=''):
        try:
            supplier = Supplier.objects.get(cnpj=supplier_cnpj)

            supplier.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Supplier.DoesNotExist:
            return Response({"message": "Fornecedor não registrado!"}, status=status.HTTP_404_NOT_FOUND)


class LoginSupplierView(APIView):
    def post(self, request):
        serializer = LoginSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]

            # DATA E HORA LOGADAS:
            date_logged = datetime.now()
            log_adm_view = datetime.strftime(date_logged, "%d-%m-%Y às %H:%M:%S")

            #VERIFICAÇÃO SE USUÁRIO É SUPER_USER:
            if user.is_super_user is True or user.is_admin is True:
                return Response({'token': token.key,
                'super_user': user.is_super_user,
                'is_admin': user.is_admin,
                'cnpj': user.cnpj,
                })
            
            # CÁLCULO VALIDADE ASSINATURA:
            signature_vality = user.signature_vality
            date_signed = datetime.strptime(signature_vality, "%Y-%m-%dT%H:%M:%S.%fZ")

            date_now = datetime.now()

            result = date_signed - date_now

            signature_in_miliseconds = date_signed.timestamp()

            if result.days >= 0:
                if result.days > 15:
                    user.login_dates.create(date_logged=log_adm_view)
                    user.save()
                    return Response({'token': token.key,
                                    'signature_vality': signature_in_miliseconds, 
                                    'cnpj': user.cnpj,
                                    })

                elif result.days <= 15:
                    user.login_dates.create(date_logged=log_adm_view)
                    user.save()
                    return Response({"message": "Assinatura perto de vencer! Contatar suporte.", 
                                     'token': token.key, 
                                     'signature_vality': signature_in_miliseconds, 
                                     'cnpj': user.cnpj, 
                                     })
            
            else:
                return Response({"message": "Assinatura vencida! Contatar suporte."}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({"message": "Fornecedor não encontrado! Verificar dados."}, status=status.HTTP_404_NOT_FOUND)


class AskChangePasswordMailView(APIView):
    def post(self, request):
        serializer = AskChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # VARIÁVEL SENHA PROVISÓRIA:
        reducedUUID = str(uuid.uuid4())[0:8] # E COMO GARANTIR QUE ELA TERÁ UM PRAZO?

        # FORMATAÇÃO DE DATA:
        dia = (datetime.now()).strftime("%d/%m/%Y")
        horas = (datetime.now()).strftime("%H:%M:%S")

        # PARA OBTER USERNAME PELO EMAIL:
        object = Supplier.objects.get(email=request.data['email'])

        # MUDANÇA SENHAS ATUAL E PROVISÓRIA:
        object.password_provisional = reducedUUID
        object.set_password(str(uuid.uuid4()))
        object.save()

        # LINKS:
        link_change_password = "http://dev-bi-abkura.s3-website-us-east-1.amazonaws.com/changepassword"
        # link_change_password = "http://localhost:3000/changepassword"

        supplier_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Olá, %s! Recebemos seu pedido por nova senha.</p>
                    <p>Segue abaixo a senha provisória mais o link para alteração de senha:</p>
                    <br>
                    <p>Senha provisória: %s </p>
                    <p>Link para alteração de senha <a href="%s">aqui</a></p>
                    <br>
                    <p>Por favor, não responda este e-mail. Ele é enviado de forma automática.<p>
                    <p>Atenciosamente,</p>
                    <h3>EMPRESA</h3>
                </body>
            </html>
        """ % (object.username, reducedUUID, link_change_password)

        admin_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Notificação: O(A) usuário(a) %s solicitou troca de senha às %s em %s.</p>
                    <p>Segue abaixo a senha provisória mais o link para alteração de senha:</p>
                    <br>
                    <p>Senha provisória de %s: %s </p>
                    <br>
                    
                    <h3>EMPRESA</h3>
                </body>
            </html>
        """ % (object.username, horas, dia, object.username, reducedUUID)

        send_mail(
            "Pedido troca de senha usuário(a) {a1} - Suporte EMPRESA".format(a1=object.username),
            "",
            "suporte.troca.senha.teste@gmail.com", 
            [request.data['email']], 
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


class EmailForAskChangePasswordView(APIView):
    def patch(self, request, user_email=''):
        try:
            user = Supplier.objects.get(email=user_email)
            if user:
                if user.asked_change_password == False:
                    user.asked_change_password = True
                    user.save(update_fields=['asked_change_password'])
                    serialized = RegisterSupplierSerializer(user)
                    return Response(serialized.data, status=status.HTTP_200_OK)

                else:
                    user.asked_change_password = False
                    user.save(update_fields=['asked_change_password'])
                    
                    serialized = RegisterSupplierSerializer(user)
                    return Response(serialized.data, status=status.HTTP_200_OK)

        except Supplier.DoesNotExist:
            return Response({"message": "Usuário não encontrado! Verificar email."}, status=status.HTTP_404_NOT_FOUND)


class ChangePasswordMailView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # FORMATAÇÃO DE DATA:
        dia = (datetime.now()).strftime("%d/%m/%Y")
        horas = (datetime.now()).strftime("%H:%M:%S")

        # PARA OBTER USERNAME PELA SENHA PROVISÓRIA:
        object2 = Supplier.objects.get(password_provisional=request.data['password_provisional'])

        # DEFINIÇÃO NOVA SENHA:
        object2.set_password(request.data['new_password'])
        object2.save()

        # CONFIRMAÇÃO NOVA SENHA:
        object2.set_password(request.data['repeat_new_password'])
        object2.save()

        # LINKS:
        link_login = "http://dev-bi-abkura.s3-website-us-east-1.amazonaws.com/"
        # link_login = "http://localhost:3000/"

        supplier_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Olá, %s!</p>
                    <p>Sua senha foi atualizada com sucesso!</p>
                    <br>
                    <p>Siga agora para o <a href="%s">login</a>.</p>
                    <br>
                    <p>Por favor, não responda este e-mail. Ele é enviado de forma automática.<p>
                    <p>Atenciosamente,</p>
                    <h3>EMPRESA</h3>
                </body>
            </html>
        """ % (object2.username, link_login)

        admin_email_message = """\
            <html>
                <head></head>
                <body>
                    <p>Notificação: O(A) usuário(a) %s trocou de senha às %s em %s.</p>
                    <br>
                    <p>Nova senha de %s: %s </p>
                    <br>
                    
                    <h3>EMPRESA</h3>
                </body>
            </html>
        """ % (object2.username, horas, dia, object2.username, request.data['new_password'])

        send_mail(
            "Confirmação troca de senha usuário(a) {a1} - Suporte EMPRESA".format(a1=object2.username),
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

