from django.shortcuts import render
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_function_call(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_function_call
def index(request):
    try:
        data = get_crypto_data()
    except Exception as e:
        print(e)
        data = dict()

    data["crypto_data"] = get_crypto_data()
    return render(request, "bitcoin/index.html", data)


@log_function_call
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=2068"
    try:



# push the data from api to template
def index(request):
    try:
        data = get_crypto_data()
    except Exception as e:
        logger.error(f"Error fetching crypto data: {e}")
        data = dict()

    data["crypto_data"] = get_crypto_data()
    return render(request, "bitcoin/index.html", data)



def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=2068"
    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = []

    return data
