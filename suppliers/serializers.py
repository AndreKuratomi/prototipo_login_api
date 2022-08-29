from rest_framework import serializers


class RegisterSupplierSerializer(serializers.Serializer):
    cnpj = serializers.CharField() #PK!
    email = serializers.EmailField()
    franquia = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    sexo = serializers.CharField() # COMO COLOCAR APENAS 2 OPÇÕES??

    password = serializers.CharField(write_only=True)
    # password_provisional = serializers.CharField() # como fazer para ter duração definida??
    
    signature_created_at = serializers.DateTimeField(read_only=True) # ele pode ser registrado sem ter assinatura?
    signature_status = serializers.BooleanField()
    signature_vality = serializers.CharField()
    
    url_dashboard = serializers.URLField() # como automatizar para o PBI fornecê-lo???
    
    username = serializers.CharField()
    username_created_at = serializers.DateTimeField(read_only=True)


class LoginSupplierSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # login_logged_at = serializers.DateTimeField() #BANCO DE DADO PARA VER QUANTAS VEZES LOGOU



class MailSerializer(serializers.Serializer):
    username = serializers.CharField()


class AskChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password_provisional = serializers.CharField(read_only=True) # como fazer para ter duração definida??


class ChangePasswordSerializer(serializers.Serializer):
    password_provisional = serializers.CharField() # como fazer para ter duração definida??
    new_password = serializers.CharField() # como ele vai substituir a senha antiga??
    repeat_new_password = serializers.CharField() # como ele vai substituir a senha antiga??

