from django.shortcuts import render

class RegisterSupplierView(APIView):
    def post(self, request):
        serializer = RegisterSupplierSerializer(data=request.data)

    
    # def get(self, request):
        # para futuramente os administradores acessarem os fornecedores via API


class LoginSupplierView(APIView):
    def post(self, request):
        serializer = LoginSupplierSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.erro)
