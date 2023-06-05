from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response


class WebView(APIView):
    def post(self, request, format=None):
        proxy = '89.187.187.171:80'
        HEADERS = ({'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'})
        url = request.data.get('url')
        webpage = requests.get(url, headers=HEADERS, proxies={'http':proxy, 'https':proxy}, timeout=3)
        htmlcontent = webpage.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        text = soup.get_text()
        new_text = text.replace('\n', '').replace('\r', '').replace('\t', '')
        # print (soup.prettify())
        return Response({'status':'True', 'message':'View Product Detail',  'url':url, 'text':new_text})



class ProductView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            type = request.data.get('type')
            webpage = requests.get(url, headers=HEADERS)
            htmlcontent = webpage.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            print('hello')
            if type == "0":
                title = soup.find("span", attrs={"id":'productTitle'}).string.strip()
                price = soup.find("span", class_="a-offscreen").get_text()
                print('hello01')
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "1":
                title = soup.find("h1", class_="pr-new-br").get_text()
                price = soup.find("span", class_="prc-dsc").get_text()
                print('hello02')
                return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
            elif type == "2":
                title = soup.find("h1", class_="product-detail-info__header-name").get_text()
                price = soup.find("span", class_="money-amount__main").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
            elif type == "3":
                title = soup.find("div", class_="product__name--detail").get_text().replace('\n', '')
                price = soup.find("ins", class_="lone-price").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
            elif type == "4":
                title = soup.find("h1", class_="pdp-title").get_text().replace('\n', '')
                price = soup.find("div", class_="pdp-prices").get_text().replace('\n', '')
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "5":
                title = soup.find("div", class_="product__detail--head").get_text().replace('\n', '')
                # price = soup.find("div", class_="pdp-prices").get_text().replace('\n', '')
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'url':url})
            elif type == "6":
                title = soup.find("span", class_="prod-subtitle text-muted").get_text()
                price = soup.find("span", class_="price-sales price-sales-standard").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "7":
                title = soup.find("h1", class_="product-card__name").get_text()
                price = soup.find("div", class_="product-card__price--new d-inline-flex align-items-baseline").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "8":
                title = soup.find("h1", class_="proName").get_text()
                price = soup.find("div", class_="newPrice").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "9":
                title = soup.find("h1", class_="product-title-text").get_text()
                price = soup.find("span", class_="uniform-banner-box-price").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "10":
                title = soup.find("span", class_="prod-subtitle text-muted").get_text()
                price = soup.find("span", class_="final-price push-right text-danger").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "11":
                title = soup.find("div", class_="ProductName-module--container__3e-gi").get_text().replace('\n', '')
                price = soup.find("span", class_="Price-module--black-large__2lI2s").get_text().replace('\n', '')
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price,  'url':url})
            elif type == "12":
                title = soup.find("div", class_="product-title").get_text()
                price = soup.find("div", class_="basket-discount").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "13":
                title = soup.find("h1", class_="product-name").get_text()
                price = soup.find("span", class_="S5XGZ text-title-xl").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            elif type == "14":
                title = soup.find("span", attrs={"id":'product-name'}).string.strip()
                price = soup.find("span", attrs={"id":'offering-price'}).string.strip()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
            else:
                return Response({'status':'False', 'message':'No Product Available'})
        except AttributeError:
            return Response({'status':'False', 'message':'You are Robot. You are not authorized to see this page'})



class AmazonView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            webpage = requests.get(url, headers=HEADERS).text
            htmlcontent = webpage.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            if soup.find("span", attrs={"id":'productTitle'}).string.strip():
                title = soup.find("span", attrs={"id":'productTitle'}).string.strip()
                price = soup.find("span", class_="a-offscreen").get_text()
                return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})



class TrendyolView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="pr-new-br").get_text()
            price = soup.find("span", class_="prc-dsc").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class ZaraView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="product-detail-info__header-name").get_text()
            price = soup.find("span", class_="money-amount__main").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class USPoloView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("div", class_="product__name--detail").get_text().replace('\n', '')
            price = soup.find("ins", class_="lone-price").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'price':price, 'title':title, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class PentiView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="pdp-title").get_text().replace('\n', '')
            price = soup.find("div", class_="pdp-prices").get_text().replace('\n', '')
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})



class LTBView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("div", class_="product__detail--head").get_text().replace('\n', '')
            # price = soup.find("div", class_="pdp-prices").get_text().replace('\n', '')
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})



class SephoraView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("span", class_="prod-subtitle text-muted").get_text()
            price = soup.find("span", class_="price-sales price-sales-standard").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class DefactoView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="product-card__name").get_text()
            price = soup.find("div", class_="product-card__price--new d-inline-flex align-items-baseline").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class N11View(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="proName").get_text()
            price = soup.find("div", class_="newPrice").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


########################################################################################################


class AliExpressView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="product-title-text").get_text()
            price = soup.find("span", class_="uniform-banner-box-price").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})



class MorphioView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("span", class_="prod-subtitle text-muted").get_text()
            price = soup.find("span", class_="final-price push-right text-danger").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class HMView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("div", class_="ProductName-module--container__3e-gi").get_text().replace('\n', '')
            price = soup.find("span", class_="Price-module--black-large__2lI2s").get_text().replace('\n', '')
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price,  'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class LCView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("div", class_="product-title").get_text()
            price = soup.find("div", class_="basket-discount").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class MangoView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("h1", class_="product-name").get_text()
            price = soup.find("span", class_="S5XGZ text-title-xl").get_text()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})


class HespiburadaView(APIView):
    def post(self, request, format=None):
        try:
            HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
            url = request.data.get('url')
            page = requests.get(url, headers=HEADERS).text
            soup = BeautifulSoup(page, "html.parser")
            title = soup.find("span", attrs={"id":'product-name'}).string.strip()
            price = soup.find("span", attrs={"id":'offering-price'}).string.strip()
            return Response({'status':'True', 'message':'View Product Detail', 'title':title, 'price':price, 'url':url})
        except AttributeError:
            return Response({'status':'False', 'message':'No Product Available'})