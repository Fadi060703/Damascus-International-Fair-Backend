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
