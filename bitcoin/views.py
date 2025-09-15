from django.shortcuts import render
from django.conf import settings
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_function_call(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} finished")
        return result
    return wrapper


@log_function_call
def index(request):
    """Main view to display cryptocurrency data"""
    try:
        crypto_data = get_crypto_data()
        context = {
            'crypto_data': crypto_data
        }
    except Exception as e:
        logger.error(f"Error fetching crypto data: {e}")
        context = {
            'crypto_data': [],
            'error': str(e)
        }

    return render(request, "bitcoin/index.html", context)


@log_function_call
def get_crypto_data():
    """Fetch cryptocurrency data from CoinMarketCap API"""
    api_url = settings.COINMARKETCAP_API_URL
    api_key = settings.COINMARKETCAP_API_KEY
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    
    parameters = {
        'start': '1',
        'limit': '100',  # Limit to top 100 cryptocurrencies
        'convert': 'USD'
    }
    
    try:
        response = requests.get(api_url, headers=headers, params=parameters)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = response.json()
        
        # Extract the data array from the response
        if 'data' in data:
            return data['data']
        else:
            logger.error(f"Unexpected API response format: {data}")
            return []
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return []
    except Exception as e:
        logger.error(f"Error processing API response: {e}")
        return []