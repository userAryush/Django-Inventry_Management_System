from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product_type,Product,Department, Sell
from .serializer import Product_typeSerializer,DepartmentSerializer,ProductSerializer,SellSerializer

from rest_framework.decorators import api_view
from django.contrib.auth import authenticate # email ra pass check garne logic cha
from rest_framework.authtoken.models import Token #toke banauna token model bata query garna paro


# Create your views here.

@api_view(['POST'])
def login(request):
    
    # user le req gareko data leko to check
    email = request.data.get('email')
    password = request.data.get('password')
    
    #check
    user =authenticate(username = email, password = password) #if matched return that user else none
    
    if user == None:
        return Response('Invalid credentials!')
    else:
        #token create
        #response ma token send
        token,_ = Token.objects.get_or_create(user=user)#authenticate le nikaleko user ko token create garna lageko creatematra garo vane harek choti create garne vo so get_or_create ra esle duita value return garne vo token and bool
        
        return Response(token.key)
        
        
    


class Product_typeViewSet(ModelViewSet):
    queryset = Product_type.objects.all()
    serializer_class = Product_typeSerializer
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer