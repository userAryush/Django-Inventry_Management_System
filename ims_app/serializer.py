from rest_framework.serializers import ModelSerializer


from .models import Product_type, Department,Product, Sell, User,purchase
from django.contrib.auth.models import Group
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','groups']# ya grp halesi aba user data create huda group field ni aaune vo
        
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class Product_typeSerializer(ModelSerializer):
    class Meta:
        model = Product_type
        fields = '__all__'  
        
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class SellSerializer(ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'
        
        
class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = purchase
        fields = '__all__'