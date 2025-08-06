from django.urls import path 
from .views import * 

urlpatterns = [ 
    path( 'articles' , ListArticlesView.as_view() , name = 'list-article' ) , 
    path( 'articles/<int:pk>' , ArticleDetailsView.as_view() , name = 'article-detail' ) ,
    path( 'category' , ListCategoryView.as_view() , name = 'cat-list' ) ,
    path( 'category/<int:pk>' , CategoryView.as_view() , name = 'cat-detail' ) ,  
    path( 'participants' , ListCompanyView.as_view() , name = 'list-company' ) , 
    path( 'participants/<int:pk>' , CompanyDetailView.as_view() , name = 'company-detail' ) , 
    path( 'offers' , ListOfferView.as_view() , name = 'offer-list' ) , 
    path( 'offers/<int:pk>' , OfferDetailView.as_view() , name = 'offer-detail' ) , 
]