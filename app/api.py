from .models import *
from rest_framework import viewsets,permissions
from .serializers import ProductInventorySerializer,ClientSerializer,RolesSerializer,CollaboratorSerializer,SalesSerializer,SalesDetailSerializer

#TODO: Crear los viewsets para los serializers  

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductsInventory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductInventorySerializer
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientSerializer

class RolesViewset(viewsets.ModelViewSet):
    queryset = Roles
    permission_classes = [permissions.AllowAny]
    serializer_class = RolesSerializer

class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CollaboratorSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalesSerializer
    
class SalesDetailViewSet(viewsets.ModelViewSet):
    queryset = SalesDetails.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalesDetailSerializer
    