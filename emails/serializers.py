from rest_framework import serializers
from .models import UserMail, AdminMail


class UserMailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserMail
        fields = ['subject', 'message', 'sender', 'receiver']
    #  = serializers.CharField()
    #  = serializers.CharField()
    #  = serializers.EmailField()
    #  = serializers.ListField()


class AdminMailSerializers(serializers.Serializer):
    class Meta:
        model = AdminMail
        fields = '__all__'
