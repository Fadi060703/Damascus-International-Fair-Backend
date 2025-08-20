from django.shortcuts import render
from .models import * 
from .serializers import * 
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status 
# Create your views here.


class CoordDetailView( APIView ) :
    serializer_class = CoordinatesSerialzier
    def get( self , request : Request , pk : int ) :
        data = Coordinates.objects.get( pk = pk ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
class ListArticlesView( APIView ) :
    serializer_class = ArticleMinimalSerializer 

    def get( self , request : Request ) :
        data = Article.objects.all() 
        serializer = self.serializer_class( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
class ArticleDetailsView( APIView ) :
    serializer_class = ArticleSerializer 

    def get( self , request : Request , pk : int ) :
        data = Article.objects.get( pk = pk ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
class ListCategoryView( APIView ) :
    serializer_class = FieldSerializer 

    def get( self , request : Request ) :
        data = CompanyBusField.objects.all() 
        serializer = self.serializer_class( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
class CategoryView( APIView ) :
    serializer_class = FieldSerializer 

    def get( self , request : Request , pk : int ) :
        data = CompanyBusField.objects.get( pk = pk ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 

class ListCompanyView( APIView ) :
    serializer_class = CompanyMinimalSerializer
    
    def get( self , request : Request ) :
        data = ParticipantCompany.objects.all() 
        serializer = self.serializer_class( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    

class CompanyDetailView( APIView ) :
    serializer_class = CompanySerializer 

    def get( self , request : Request , pk : int ) :
        data = ParticipantCompany.objects.get( pk = pk ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 

class ListOfferView( APIView ) :
    serializer_class = OfferMinimalSerializer 

    def get( self , request : Request  ) :
        data = Offer.objects.all() 
        serializer = self.serializer_class( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 

class OfferDetailView( APIView ) :
    serializer_class = OfferSerializer
    def get( self , request : Request , pk : int ) :
        data = Offer.objects.get( pk = pk ) 
        serializer = self.serializer_class( data )
        return Response( data = serializer.data , status = status.HTTP_200_OK )    


class ListCompanyProductsView( APIView ) :
    serializer_class = ProductSerializer
    def get( self , request : Request , pk : int ) :
        data = Product.objects.filter( company = pk ) 
        serializer = self.serializer_class( data , many = True ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
class ProductDetailView( APIView ) :
    serializer_class = ProductSerializer 
    def get( self , request : Request , pk : int ) :
        data = Product.objects.get( pk = pk ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
class GetInfoView( APIView ) :
    serializer_class = InfoSerializer 
    def get( self , request : Request ) :
        data = Info.objects.get( pk = 1 ) 
        serializer = self.serializer_class( data ) 
        return Response( data = serializer.data , status = status.HTTP_200_OK ) 
    
