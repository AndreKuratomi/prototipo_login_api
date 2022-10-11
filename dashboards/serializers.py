from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    is_favorite = serializers.BooleanField(default=False)
    name = serializers.CharField()
    url = serializers.URLField()

    created_at = serializers.DateTimeField(read_only=True)
    last_clicked = serializers.DateTimeField(read_only=True)
    
    supplier_owner = serializers.CharField()
