from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.exceptions import UnmatchedPasswordsException

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="iso-8601")
    updated_at = serializers.DateTimeField(read_only=True, format="iso-8601")

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        password, conf_password = validated_data.pop("password"), validated_data.pop(
            "confirm_password"
        )
        if password != conf_password:
            raise UnmatchedPasswordsException(
                "Invalid Passwords Or Passwords Not Matched"
            )

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
