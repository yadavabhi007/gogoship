from django.urls import path
from . import views


urlpatterns = [
    path('web-product/', views.WebView.as_view(), name='web-product'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('amazon-product/', views.AmazonView.as_view(), name='amazon-product'),
    path('trendyol-product/', views.TrendyolView.as_view(), name='trendyol-product'),
    path('zara-product/', views.ZaraView.as_view(), name='zara-product'),
    path('uspolo-product/', views.USPoloView.as_view(), name='uspolo-product'),
    path('penti-product/', views.PentiView.as_view(), name='penti-product'),
    path('hm-product/', views.HMView.as_view(), name='hm-product'),
    path('ltb-product/', views.LTBView.as_view(), name='ltb-product'),
    path('morphio-product/', views.MorphioView.as_view(), name='morphio-product'),
    path('sephora-product/', views.SephoraView.as_view(), name='sephora-product'),
    path('defacto-product/', views.DefactoView.as_view(), name='defacto-product'),
    path('lc-product/', views.LCView.as_view(), name='lc-product'),
    path('mango-product/', views.MangoView.as_view(), name='mango-product'),
    path('hespiburada-product/', views.HespiburadaView.as_view(), name='hespiburada-product'),
    path('n11-product/', views.N11View.as_view(), name='n11-product'),
    path('aliexpress-product/', views.AliExpressView.as_view(), name='aliexpress-product'),
]