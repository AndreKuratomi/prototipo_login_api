from rest_framework import serializers

class UserMailSerializers(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    sender = serializers.EmailField()
    receiver = serializers.ListField()


class AdminMailSerializers(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    sender = serializers.EmailField()
    receiver = serializers.ListField()
