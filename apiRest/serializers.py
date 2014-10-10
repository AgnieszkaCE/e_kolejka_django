from pokoje.models import Pokoj
from django.contrib.auth.models import User

from rest_framework import serializers

class PokojSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pokoj
        fields = ('id', 'nazwa')
        
class NumerSerializer(serializers.ModelSerializer):
    
    jak_jest = serializers.CharField(max_length=100)
    cosik = serializers.CharField(max_length=100)
    class Meta:
        model = Pokoj
        fields = ('cosik', 'jak_jest')
    
        
class LoginSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(max_length=100)
    status = serializers.BooleanField()
    class Meta:
        fields = ('tag', 'status')
    
    
    
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username')