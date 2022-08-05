from django.core.mail import mail_admins, send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from emails.serializers import MailSerializers

import ipdb


class MailView(APIView):
    def post(self, request):
        serializer = MailSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # ipdb.set_trace()
        send_mail(request.data['subject_supplier'], request.data['message_supplier'], request.data['sender'], [request.data['receiver']])
        mail_admins(request.data['subject_admin'], request.data['message_admin'])

        return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)

