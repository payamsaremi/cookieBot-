from django.db.models import fields
from rest_framework import serializers
from core.models import Choice, Question, question

from .choice import ChoiceSerializer

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default = serializers.CurrentUserDefault())
    choices = ChoiceSerializer(many = True)

    class Meta:
        model = Question
        fields = ["id", "text", "creation_date", "start_date", "end_date", "choices", "owner"]

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(question = question, **choice)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop("choices")
        instance.text = validated_data.get("text", instance.text)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id = choice["id"])
                    c.text = choice.get("text", c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(question = instance, **choice)
                keep_choices.append(c.id)
        for choice in instance.choices.all():
            if choice.id not in keep_choices:
                choice.delete()
        
        return instance

