from rest_framework import serializers
from .models import Mail


class MailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'
