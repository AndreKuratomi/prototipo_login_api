from rest_framework import serializers

class RegisterSupplierSerializer(serializers.Serializer):
    cnpj = serializers.CharField(read_only=True, required=True) #PK!
    email = serializers.CharField(required=True)
    franquia = serializers.CharField(required=True)
    fist_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    password = serializers.CharField(required=True)
    # password_provisional = serializers.CharField(required=True) # como fazer para ter duração definida??
    
    signature_created_at = serializers.DateTimeField(read_only=True) # ele pode ser registrado sem ter assinatura?
    signature_status = serializers.BooleanField(required=True)
    signature_vality = serializers.CharField(required=True)
    
    url_dashboard = serializers.CharField(required=True) # como automatizar para o PBI fornecê-lo???
    
    username = serializers.CharField(required=True)
    username_created_at = serializers.DateTimeField(read_only=True)


class LoginSupplierSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    # email = serializers.CharField(required=True) que tal colocar como opçao email ou username? e como fazer?

    password = serializers.CharField(required=True)


class AskChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True) # e precisa?
    email = serializers.CharField(required=True)

    password_provisional = serializers.CharField(required=True) # como fazer para ter duração definida??


class ChangePasswordSerializer(serializers.Serializer):
    password_provisional = serializers.CharField(required=True) # como fazer para ter duração definida??
    new_password = serializers.CharField(required=True) # como ele vai substituir a senha antiga??
    repeat_new_password = serializers.CharField(required=True) # como ele vai substituir a senha antiga??

