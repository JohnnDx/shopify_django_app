from django.apps import AppConfig
import os


class ShopifyAppConfig(AppConfig):
    name = 'shopify_app'
    # Replace the API Key and Shared Secret with the one given for your
    # App by Shopify.
    #
    # To create an application, or find the API Key and Secret, visit:
    # - for private Apps:
    #     https://${YOUR_SHOP_NAME}.myshopify.com/admin/api
    # - for partner Apps:
    #     https://www.shopify.com/services/partners/api_clients
    #
    # You can ignore this file in git using the following command:
    #   git update-index --assume-unchanged shopify_settings.py
    SHOPIFY_API_KEY = '52da6581254236fc44ea61c07c8156c0'
    SHOPIFY_API_SECRET = '1891280cb77da21c75caac145486417b'

    # SHOPIFY_API_KEY = '09af22b423e46773f35b300d7d0c994b'
    # SHOPIFY_API_SECRET = '6d8f007ca207134502befad45aa43c97'

    # SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
    # SHOPIFY_API_SECRET = os.getenv('SHOPIFY_API_SECRET')

    # API_VERSION specifies which api version that the app will communicate with
    SHOPIFY_API_VERSION = os.environ.get('SHOPIFY_API_VERSION', 'unstable')

    # See http://api.shopify.com/authentication.html for available scopes
    # to determine the permisssions your app will need.
    # SHOPIFY_API_SCOPE = os.environ.get('SHOPIFY_API_SCOPE', 'read_themes').split(',')
    SHOPIFY_API_SCOPE = ['read_themes', 'write_themes']
 