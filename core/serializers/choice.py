from django.db import models
from django.db.models.fields import IntegerField
from rest_framework import serializers

from core.models import Choice

class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)

    class Meta:
        model = Choice
        fields = ["id", "text", "question"]
        read_only_fields = ("question",)
        