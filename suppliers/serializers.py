from rest_framework import serializers


class LoggedSupplierSerializer(serializers.Serializer):
    date_logged = serializers.CharField()


class RegisterSupplierSerializer(serializers.Serializer):
    cnpj = serializers.CharField() #PK!
    email = serializers.EmailField()
    franquia = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    password = serializers.CharField(write_only=True)
    # password_provisional = serializers.CharField() # como fazer para ter duração definida??
    
    signature_created_at = serializers.DateTimeField(read_only=True) # ele pode ser registrado sem ter assinatura?
    signature_status = serializers.BooleanField()
    signature_vality = serializers.CharField()
    is_super_user = serializers.BooleanField()
    
    url_dashboard = serializers.URLField() # como automatizar para o PBI fornecê-lo???
    
    username = serializers.CharField()
    username_created_at = serializers.DateTimeField(read_only=True)

    login_dates = LoggedSupplierSerializer(many=True, required=False)


class LoginSupplierSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # login_logged_at = serializers.DateTimeField() #BANCO DE DADO PARA VER QUANTAS VEZES LOGOU



class AskChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    password_provisional = serializers.CharField() # como fazer para ter duração definida??
    new_password = serializers.CharField()
    repeat_new_password = serializers.CharField()

