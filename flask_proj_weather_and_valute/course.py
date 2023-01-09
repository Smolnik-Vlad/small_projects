import requests
def get_course(currency: str='BYN'):
    KEY = 'YnPC0lvBKQe8prPH8uJiqIunZtRXmLPb'
    params={'apikey': KEY}
    value=requests.get('https://api.apilayer.com/currency_data/change', params=params)
    all_values=value.json()
    USD_MyCurrency=all_values['quotes'][f'USD{currency}']
    return USD_MyCurrency


print(get_course('BYN'))