from rest_framework import serializers

from dashboards.serializers import DashboardSerializer


class LoggedSupplierSerializer(serializers.Serializer):
    date_logged = serializers.CharField()


class RegisterSupplierSerializer(serializers.Serializer):
    cnpj = serializers.CharField() #PK!
    email = serializers.EmailField()
    franquia = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    password = serializers.CharField(write_only=True)
    # password_provisional = serializers.CharField() # COMO FAZER PARA TER DURAÇÃO DEFINIDA??
    
    signature_created_at = serializers.DateTimeField(read_only=True)
    signature_vality = serializers.CharField(required=False)
    
    is_admin = serializers.BooleanField()
    is_super_user = serializers.BooleanField()
    
    username = serializers.CharField()
    username_created_at = serializers.DateTimeField(read_only=True)

    login_dates = LoggedSupplierSerializer(many=True, required=False)
    dashboards = DashboardSerializer(many=True, read_only=True)


class LoginSupplierSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class AskChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ChangePasswordSerializer(serializers.Serializer):
    password_provisional = serializers.CharField() # COMO FAZER PARA TER DURAÇÃO DEFINIDA??
    new_password = serializers.CharField()
    repeat_new_password = serializers.CharField()

