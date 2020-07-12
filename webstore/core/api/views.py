from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from core.api.serializers import ProductSerializer, ClientSerializer
from core.models import Product, Client


class ProductCreateListView(APIView):
    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_404_NOT_FOUND)


class ClientCreateListView(APIView):
    def get(self, request):
        try:
            clients = Client.objects.filter(active=True)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            data = request.data
            serializer = ClientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailActionsView(APIView):
    def get_client(self, pk):
        return get_object_or_404(Client, pk=pk, active=True)

    def get(self, request, pk):
        try:
            client = self.get_client(pk)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            client = self.get_client(pk)
            serializer = ClientSerializer(client, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            client = self.get_client(pk)
            client.delete()
            return Response({'mensagem': 'cliente removido'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({'mensagem': f'{ex}'}, status=status.HTTP_400_BAD_REQUEST)
