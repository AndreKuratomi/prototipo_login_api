from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.view import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import AuthenticationMiddleware

from suppliers.serializers import RegisterSupplierSerializer, LoginSupplierSerializer, 

from .models import Supplier



class RegisterSupplierView(APIView):
    def post(self, request):
        serializer = RegisterSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_supplier = RegisterSupplier.objrts.filter(username=serializer.validated_data['email']).exists()
        if find_supplier is True:
            return Response({"message": "Fornecedor já registrado!"}, status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        supplier = Supplier.objects.create_user(**serializer.validated_data)
        serializer = RegisterSupplierSerializer(supplier)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # def get(self, request):
        # users = RegisterSupplier.objects.all()
        # serializer = RegisterSupplierSerializer(users, many=True)

        # return Response(serializer.data)
        # para futuramente os administradores acessarem os fornecedores via API


class LoginSupplierView(APIView):
    def post(self, request):
        serializer = LoginSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user in not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
