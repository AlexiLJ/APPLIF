from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated #Authentication
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets, status
from .models import Product, Offer
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    
    def __init__(self, ser_l=ProductSerializer, mod=Product):
        self.ser_l = ser_l
        self.mod = mod

    permission_classes = (IsAuthenticated,) # Authentication
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    
    def get(self, request): 
        products = self.mod.objects.all()
        serializer = self.ser_l(products, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.ser_l(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None): #/api/products/<str:id>
        product = self.mod.objects.get(id=pk)
        serializer = self.ser_l(product)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/products/<str:id>
        product = self.mod.objects.get(id=pk)
        serializer = self.ser_l(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):  #/api/products/<str:id>
        product = self.mod.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OfferViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,) # Authentication
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    def get(self, request): 
        products = Product.objects.all()
        
        serializer = OfferSerializer(products, many=True)
        #f serializer.data.is_valid():

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = OfferSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = OffertSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        

    def destroy(self, request, pk=None):  #/api/products/<str:id>
        Offer = Offer.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)