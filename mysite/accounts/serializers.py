from accounts.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data["password"])
        user.save()
        return user
