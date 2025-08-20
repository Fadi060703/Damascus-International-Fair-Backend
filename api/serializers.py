from rest_framework import serializers
from .models import * 

class CoordinatesSerialzier( serializers.ModelSerializer ) :
    class Meta :
        model = Coordinates 
        fields = [ 'sectionNumber' , 'long' , 'alt' ] 

class ArticleMinimalSerializer( serializers.ModelSerializer ) :
    class Meta : 
        model = Article
        fields = [ 'id' , 'headline' , 'created_at' ] 

class ArticleSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Article 
        fields = [ 'id' , 'headline' , 'articleText' , 'image' , 'created_at' ] 

class FieldSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = CompanyBusField 
        fields = [ 'id' , 'name' ] 

class CompanyMinimalSerializer( serializers.ModelSerializer ) :
    FieldSerializer()
    class Meta :
        model = ParticipantCompany 
        fields = [ 'id' , 'name' , 'category' , 'logo' ] 

class CompanySerializer( serializers.ModelSerializer ) :
    FieldSerializer()
    class Meta :
        model = ParticipantCompany 
        fields = [ 'name' , 'category' , 'description' , 'logo' , 'phoneNumber' , 'email' , 'map' ] 

class OfferMinimalSerializer( serializers.ModelSerializer ) :
    CompanySerializer()
    class Meta : 
        model = Offer 
        fields = [ 'id' , 'company' , 'name' ]

class OfferSerializer( serializers.ModelSerializer ) :
    CompanySerializer()
    class Meta :
        model = Offer 
        fields = [ 'id' , 'company' , 'name' , 'description' ] 

class ProductMinimalSerializer( serializers.ModelSerializer ) :
    CompanySerializer()
    class Meta :
        model = Product
        fields = [ 'id' , 'name' , 'company' ] 

class ProductSerializer( serializers.ModelSerializer ) :
    CompanySerializer() 
    class Meta : 
        model = Product 
        fields = [ 'id' , 'name' , 'company' , 'description' , 'image' ]  

class InfoSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Info 
        fields = [ 'about' , 'times' , 'entries' , 'media' , 'transportation' ] 

class FeedbackSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Feedack
        fields = [ 'fullName' , 'email' , 'phoneNumber' , 'text' ] 