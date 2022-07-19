from rest_framework import serializers

class SupplierSerializer(serializers.Serializer):
    cnpj = serializers.CharField(read_only=True) #PK!
    email = serializers.CharField()
    franquia = serializers.CharField()
    fist_name = serializers.CharField()
    last_name = serializers.CharField()

    password = serializers.CharField()
    password_provisional = serializers.CharField() # como fazer para ter duração definida??
    
    signature_created_at = serializers.DateTimeField(read_only=True)
    signature_status = serializers.BooleanField()
    signature_vality = serializers.CharField()
    
    url_dashboard = serializers.CharField() # como automatizar para o PBI fornecê-lo???
    
    username = serializers.CharField()
    username_created_at = serializers.DateTimeField(read_only=True)

