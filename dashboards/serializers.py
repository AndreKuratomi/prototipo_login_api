from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    id = serializers.IntegerField() #PK!
    category = serializers.Charfield()
    is_favorite = serializers.BooleanField(default=false)
    name = serializers.Charfield()
    url = serializers.URLField()
    created_at = serializers.DateTimeField(read_only=True)
    
    # supplier = serializers.ForeignKey(Supplier, on_delete=serializers.CASCADE)

    # REQUIRED_FIELDS = ['__all__']
