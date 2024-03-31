import json
import requests
from config import keys

class ConvertionException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def conserv( quote : str, base : str, amoung : str):


        if quote == base:
            raise ConvertionException("Нельзя перевести валюту саму в себя!")


        try:
            keys[quote] == keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            keys[base] == keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amoung == float(amoung)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amoung}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_amoung = float(amoung)*json.loads(r.content)[keys[base]]
        return total_amoung