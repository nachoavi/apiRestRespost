from rest_framework import serializers
from .models import *

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInventory
        #fields = ('id','name','price','description','stock')
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id','ADMINISTRATOR','NORMAL_USER')
        read_only_fields = ('ADMINISTRATOR','NORMAL_USER')
        
class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'
        
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ('id','date','client')
        read_only_fields = ('date',)

class SalesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDetails
        fields = '__all__'
         
        