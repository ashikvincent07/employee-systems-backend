from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

from employees.serializers import UserSerializer, EmployeeSerializer
from employees.models import Employee



class UserSignUpView(APIView):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        data = request.data

        serializer_instance = self.serializer_class(data=data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
        



class EmployeeCreateListView(APIView):

    serializer_class = EmployeeSerializer

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):

        serializer_instance = self.serializer_class(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(owner=request.user)

            return Response(data=serializer_instance.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request, *args, **kwargs):

        employee_list = get_list_or_404(Employee, owner=request.user)

        serializer_instance = self.serializer_class(employee_list, many=True)

        return Response(data=serializer_instance.data, status=status.HTTP_200_OK)

        


