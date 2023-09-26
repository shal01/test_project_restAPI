from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True,required=False)

    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    model=User
    fields=['urls','id','username','email','first_name','last_name','email','password']