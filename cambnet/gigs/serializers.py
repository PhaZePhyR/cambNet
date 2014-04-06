from rest_framework import serializers

from .models import Gig, SignUp

class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = ('name', 'description', 'uniform', 'start_datetime', 'end_datetime', 'extra_credit', 'cars')
        depth = 1

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('user', 'gig', 'stamp')
        depth = 2