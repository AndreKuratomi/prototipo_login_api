from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from emails.serializers import UserMailSerializers, AdminMailSerializers

import ipdb


class UserMailView(APIView):
    def post(self, request):
        serializer = UserMailSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # ipdb.set_trace()
        send_mail(request.data['subject'], request.data['message'], request.data['sender'], [request.data['receiver']])

        return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)


class AdminMailView(APIView):
    def post(self, request):
        serializer = AdminMailSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        send_mail(request.data['subject'], request.data['message'], request.data['sender'], [request.data['receiver']])

        return Response({"message": "Email successfully sent"}, status=status.HTTP_200_OK)
