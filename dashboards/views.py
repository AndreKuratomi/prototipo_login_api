from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime, timedelta

from .models import Dashboard
from .serializers import DashboardSerializer
from suppliers.models import Supplier

import ipdb


class RegisterDashboardView(APIView):
    def post(self, request):
        serializer = DashboardSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        find_dashboard_url = Dashboard.objects.filter(url=serializer.validated_data['url']).exists()
        if find_dashboard_url is True:
            return Response({"message": "Dashboard já registrada!"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # dashboard = Dashboard.objects.create(**serializer.validated_data)

        user = Supplier.objects.filter(cnpj = serializer.validated_data['supplier_owner'])
        if user.exists() is False:
            return Response({"message": "Fornecedor não encontrado! Verificar dados."}, status=status.HTTP_404_NOT_FOUND)

        new_dashboard = user[0].dashboards.create(**serializer.validated_data)
        user[0].save()

        serializer = DashboardSerializer(new_dashboard)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        all_dashboards = Dashboard.objects.all()
        serializer = DashboardSerializer(all_dashboards, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DashboardByIdView(APIView):
    def get(self, request, dashboard_id=''):
        try:
            dashboard = Dashboard.objects.get(id=dashboard_id)
            # PESQUISAR prefetch_related() PARA POSSIBILIDADE DE MAIS DE UMA URL!
            serialized = DashboardSerializer(dashboard)

            return Response(serialized.data, status=status.HTTP_200_OK)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, dashboard_id=''):
        serializer = DashboardSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        super_user = Supplier.objects.filter(is_super_user=True)
        if super_user is False:
            return Response({"message": "Fornecedor não encontrado! Verificar dados."}, status=status.HTTP_404_NOT_FOUND)

        try:
            updated_dashboard = Dashboard.objects.filter(id=dashboard_id).update(**serializer.validated_data)
            updated = Dashboard.objects.get(id=dashboard_id)

            serialized = DashboardSerializer(updated)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, dashboard_id=''):
        try:
            dashboard = Dashboard.objects.get(id=dashboard_id)

            dashboard.delete()
            # Dashboard.remove()??

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)


class DashboardByCategoryView(APIView):
    def get(self, request, dashboard_category=''):
        try:
            adjusted_query = dashboard_category.strip().lower()

            dashboard = Dashboard.objects.filter(category=adjusted_query)
            # ipdb.set_trace()
            if dashboard.count() > 0:
                serialized = DashboardSerializer(dashboard, many=True)

                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Nada encontrado!"}, status=status.HTTP_404_NOT_FOUND)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)


class LastVisitedDashboardView(APIView):
    def patch(self, request, dashboard_id=''):
        serializer = DashboardSerializer(data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        super_user = Supplier.objects.get(is_super_user=True)
        if super_user is False:
            return Response({"message": "Fornecedor não encontrado! Verificar dados."}, status=status.HTTP_404_NOT_FOUND)

        try:
            update = Dashboard.objects.get(id=dashboard_id)
            update.last_clicked = datetime.now()
            update.save(update_fields=['last_clicked'])

            last_list = super_user.last_visited_dashboards
            list_content = last_list.all()

            if list_content.count() < 3:
                last_list.add(update)
                super_user.save()

            elif list_content.count() == 3:
                last = str(list_content[0].last_clicked)[0:26]
                date_now = datetime.now()
                date_clicked = datetime.strptime(last, "%Y-%m-%d %H:%M:%S.%f")

                final_result = date_now - date_clicked


                for value in list_content:
                    date_now = datetime.now()
                    date_clicked = datetime.strptime(str(value.last_clicked)[0:26], "%Y-%m-%d %H:%M:%S.%f")

                    result_1 = date_now - date_clicked
                    print(result_1)

                    if result_1 > final_result:
                        last = value
                        print(last)

                last_list.remove(last)
                last_list.add(update)

                super_user.save()

            last_list.order_by('last_clicked').reverse()
            # ipdb.set_trace()
            # super_user.save()


            serialized = DashboardSerializer(update)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)


class DashboardEditFavoriteView(APIView):
    def patch(self, request, dashboard_id=''):

        super_user = Supplier.objects.filter(is_super_user=True)
        if super_user is False:
            return Response({"message": "Fornecedor não encontrado! Verificar dados."}, status=status.HTTP_404_NOT_FOUND)

        # serializer = DashboardSerializer(data=request.data, partial=True)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            dashboard = Dashboard.objects.get(id=dashboard_id)
            print(dashboard.is_favorite)
            if dashboard.is_favorite == False:
                dashboard.is_favorite = True
                dashboard.save(update_fields=['is_favorite'])

                super_user[0].favorite_dashboards.add(dashboard)
                super_user[0].save()

                serialized = DashboardSerializer(dashboard)

                return Response(serialized.data, status=status.HTTP_200_OK)

            else:
                dashboard.is_favorite = False
                dashboard.save(update_fields=['is_favorite'])

                super_user[0].favorite_dashboards.remove(dashboard)

                serialized = DashboardSerializer(dashboard)

                return Response(serialized.data, status=status.HTTP_200_OK)

        except Dashboard.DoesNotExist:
            return Response({"message": "Dashboard não registrado!"}, status=status.HTTP_404_NOT_FOUND)
