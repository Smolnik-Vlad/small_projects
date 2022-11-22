from flask import Flask, send_from_directory
from req_city_weather import get_weather
from course import get_course
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    weather=get_weather()
    currency=get_course()

    return {'weather': weather, 'currency': currency}

@app.route('/weather')
def weather_for_Minsk():
    return get_weather()

@app.route('/weather/<string:city>')
def weather_in_specified_city(city='Minsk'):
    weather=get_weather(city=city)
    return weather

@app.route('/currency')
def currency_BYN():
    return {'currency': get_course()}

@app.route('/currency/<string:currency>')
def currency_by_currency(currency):
    return {'currency': get_course(currency)}

@app.route('/dataset_generator/<string:city>/<string:currency>')
def dataset_generator(city, currency):
    info_about_weather = get_weather(city)
    info_about_currency = get_course(currency)
    collected_my_info = [[{currency:info_about_currency['start_rate']},
                        {city:
                            [info_about_weather['weather']['main'],
                             info_about_weather['main']['temp']]
                        }]
                        ]
    with open('data.csv', 'w') as file:
        writer=csv.writer(file)
        writer.writerow(['Currency', 'City'])
        # print(info_about_weather)
        # print(info_about_currency)

    for i in collected_my_info:
        with open('data.csv', 'a') as file:
            writer=csv.writer(file)
            writer.writerow(i)


    return collected_my_info #"""send_from_directory(directory='D:\work\python_project\ flask_proj', path='data.csv'),"""

if __name__ == '__main__':
    app.run(debug=True)
