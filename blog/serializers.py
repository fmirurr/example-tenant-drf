from rest_framework import serializers

from .models import SomeModel


class SomeModelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = [
            "name",
        ]
