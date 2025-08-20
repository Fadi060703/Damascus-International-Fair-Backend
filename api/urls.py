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
    path( 'coordinates/<int:pk>' , CoordDetailView.as_view() , name = 'cord-detail' ) ,
    path( 'company-products/<int:pk>' , ListCompanyProductsView.as_view() , name = 'comp-prod' ) , 
    path( 'products/<int:pk>' , ProductDetailView.as_view() , name = 'prod-detail' ) ,
    path( 'info' , GetInfoView.as_view() , name = 'inf' )
]