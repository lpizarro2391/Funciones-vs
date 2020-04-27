import requests
_ENDPOINT = "https://api.binance.com"
def _url(api):
    return _ENDPOINT+api
def get_price(cripto):
    return request.get(_url("/api/v3/ticker/price?symbol="+cripto))
