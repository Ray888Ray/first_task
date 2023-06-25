from rest_framework import serializers
from webapp.models import CardGreeting


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardGreeting
        fields = ['name', 'city', 'username']

