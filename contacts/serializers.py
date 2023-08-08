from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Contact
        fields = [
            "id",
            "email",
            "name",
            "phone",
            "created_at"
        ]
        read_only_fields = ["id", "created_at"]
