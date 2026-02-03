from rest_framework import serializers

from django.contrib.auth.models import User

from employees.models import Employee


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password' : {"read_only" : True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee
        fields = "__all__"
        read_only_fields = ['owner', 'id', 'created_at']