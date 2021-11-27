from enroll.models import snippet,tags
from rest_framework import serializers

class snippetserializer(serializers.ModelSerializer):
    class Meta:
        model = snippet
        fields ='__all__'