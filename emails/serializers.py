from rest_framework import serializers

class UserMailSerializers(serializers.Serializer):
    subject = serializers.CharField(255)
    message = serializers.TextField()
    sender = serializers.EmailField(255)
    receiver = serializers.ListField(255)


class AdminMailSerializers(serializers.Serializer):
    subject = serializers.CharField(255)
    message = serializers.TextField()
    sender = serializers.EmailField(255)
    receiver = serializers.ListField(255)
