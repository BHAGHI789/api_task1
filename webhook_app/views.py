# webhook_api/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationByAccountView(APIView):
    def get(self, request, account_id):
        try:
            account = Account.objects.get(account_id=account_id)
            destinations = Destination.objects.filter(account=account)
            serializer = DestinationSerializer(destinations, many=True)
            return Response(serializer.data)
        except Account.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
