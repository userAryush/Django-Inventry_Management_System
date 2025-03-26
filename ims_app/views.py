from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Product_type,Product,Department, Sell, purchase
from .serializer import Product_typeSerializer,DepartmentSerializer,ProductSerializer,SellSerializer,UserSerializer,PurchaseSerializer,GroupSerializer

from .permissions import CustomModelPermissions 
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate # email ra pass check garne logic cha
from rest_framework.authtoken.models import Token #toke banauna token model bata query garna paro
from django.contrib.auth.hashers import make_password # password hash garne logic cha
from rest_framework.permissions import AllowAny , DjangoModelPermissions
from django.contrib.auth.models import Group


# Create your views here.

# User table ma data create garneee
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    hashed_password = make_password(password)
    request.data['password']=hashed_password
    serializer= UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User created successfully!")
    else:
        return Response(serializer.errors)
    
    
    


@api_view(['POST'])
@permission_classes([AllowAny])
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
        
@api_view(['GET'])
@permission_classes([AllowAny])
def group_listing(request):
    group_objs = Group.objects.all()
    serializer = GroupSerializer(group_objs, many=True)
    
    return Response(serializer.data)
    


class Product_typeViewSet(ModelViewSet):
    queryset = Product_type.objects.all()
    serializer_class = Product_typeSerializer
    permission_classes = [CustomModelPermissions]
    
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [CustomModelPermissions]
    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomModelPermissions]
    
class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = [CustomModelPermissions]
    
class PurchaseViewSet(ModelViewSet):
    queryset = purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [CustomModelPermissions]