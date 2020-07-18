from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if (password != password2):
            raise serializers.ValidationError({'password': "비밀번호 틀림"})
        else:
            user = User.objects.create(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
                gender=self.validated_data['gender'],
            )
            user.set_password(self.validated_data['password'])
            user.save()
            return User

    class Meta:
        model = User
        fields = ["pk", "email", "username", "password", "password2"]
