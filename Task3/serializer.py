
from rest_framework import serializers
from . models import Dynamic_fields

class Dynamic_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamic_fields
        fields = "__all__"