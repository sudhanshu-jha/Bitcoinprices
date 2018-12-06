from django.shortcuts import render
import requests


# push the data from api to template
def index(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    return render(request, "bitcoin/index.html", data)

#  function to return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=2068"
    
    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data

