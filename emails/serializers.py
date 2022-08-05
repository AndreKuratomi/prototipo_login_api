from rest_framework import serializers
from .models import Mail


class MailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


# class AdminMailSerializers(serializers.Serializer):
#     class Meta:
#         model = AdminMail
#         fields = '__all__'
