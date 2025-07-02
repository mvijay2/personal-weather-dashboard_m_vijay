from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # 🔑 Tells DRF to expect 'email' instead of 'username'

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')  # ✅ Remap email to username
        return super().validate(attrs)
