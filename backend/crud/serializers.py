from rest_framework import serializers
from .models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' # This will serialize all fields in the model