from rest_framework import serializers
from channel1.models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
