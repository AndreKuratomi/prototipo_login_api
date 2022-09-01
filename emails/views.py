# from django.core.mail import mail_admins, send_mail

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .. import RegisterSupplierSerializers

# import ipdb


# class MailView(APIView):
#     def post(self, request):
#         serializer = RegisterSupplierSerializers(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         # ipdb.set_trace()
#         send_mail(
#             "Troca de email usuário(a) {{request.data['username']}} - Suporte VestCasa", 
#             "Olá, {{request.data['username']}}! Recebemos seu pedido por nova senha. Segue abaixo a senha provisória mais o link para alteração de senha: Senha provisória: 23614163-d635; Link para alteração de senha aqui", 
#             "suporte.troca.senha.teste@gmail.com", 
#             request.data['receiver']
#             )
#         mail_admins(
#             "Aviso de troca de email - Usuário(a) {b1}".format(b1=request.data['username']), 
#             "Notificação: O(A) usuário(a) {{request.data['username']}} solicitou troca de senha às 11:32:58 em 22/07/2022. Senha provisória de {{request.data['username']}}: 23614163-d635; Vestcasa"
#             )

#         return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)

