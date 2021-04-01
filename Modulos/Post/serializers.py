from rest_framework import serializers
from . import models


class PostSerializers(serializers.ModelSerializer):
    titulo=serializers.CharField(required=True,min_length=3)
    class Meta:
        model=models.Post
        fields='__all__'