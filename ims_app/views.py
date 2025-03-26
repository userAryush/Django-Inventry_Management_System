from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product_type,Product,Department
from .serializer import Product_typeSerializer,DepartmentSerializer,ProductSerializer,SellSerializer

# Create your views here.

class Product_typeViewSet(ModelViewSet):
    queryset = Product_type.objects.all()
    serializer_class = Product_typeSerializer
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class Sell(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer