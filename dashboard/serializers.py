from .models import DataSource
from rest_framework import serializers

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = "__all__"

