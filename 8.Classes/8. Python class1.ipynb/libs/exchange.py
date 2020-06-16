# coding: utf-8
import requests

def my_sum(x, y):
    return x+y

class Rate:
    def __init__(self, diff, format_='value'):
        self.format = format_
        self.diff = diff
    
    def exchange_rates(self):

        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def make_format(self, currency): 
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        - только значение при self.format = 'value'
        Rate('value').make_format('EUR')
        79.4966
        Параметр diff (со значениями True или False), в случае значения True
        в методах курсов валют (eur, usd итд) возвращает не курс валюты,
        а изменение по сравнению в прошлым значением. 
        self.diff принимает значение True только при возврате значения курса.
        При отображении всей информации о валюте он не используется.
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                self.diff == True
                return response[currency]['Value']
            
            
        return 'Error'
    
    def eur(self):
        if self.diff:
            return 'Изменение: ', response[currency]['Value'] - response[currency]['Previous']
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        return self.make_format('AZN')
    

        

    


    




    
    
    
    