from django.db import models

# Create your models here.

class Coordinates( models.Model ) :
    sectionNumber = models.CharField( max_length = 255 ) 
    long = models.CharField( max_length = 255 ) 
    alt = models.CharField( max_length = 255 ) 

    class Meta :
        def __str__( self ) :
            return f'{ self.sectionNumber }' 

class Article( models.Model ) :
    headline = models.CharField( max_length = 255 ) 
    articleText = models.TextField() 
    image = models.ImageField( upload_to = 'media/news' ) 
    created_at = models.DateField( auto_now_add = True ) 
    class Meta :
        def __str__( self ) :
            return f'{ self.headline }'

class CompanyBusField( models.Model ) :
    name = models.CharField( max_length = 255 ) 

    def __str__( self ) :
        return self.name

class ParticipantCompany( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    category = models.ForeignKey( CompanyBusField , on_delete = models.CASCADE , related_name = 'comCat' ) 
    logo = models.ImageField( upload_to= 'media/logos' ) 
    phoneNumber = models.CharField( max_length = 255 ) 
    description = models.TextField() 
    email = models.EmailField() 
    map = models.ForeignKey( Coordinates , on_delete = models.CASCADE , related_name = 'coord' )  

    class Meta :
        def __str__( self ) :
            return f'{ self.name + self.category}' 
        
class Offer( models.Model ) :
    company = models.ForeignKey( ParticipantCompany , on_delete = models.CASCADE , related_name = 'comOffer' ) 
    name = models.CharField( max_length = 255 ) 
    description = models.TextField() 

    class Meta :
        def __str__( self ) :
            return f'{ self.company + '' + self.name }' 