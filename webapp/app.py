from flask import Flask  
from datetime import date
import os, requests, re
app = Flask(__name__)

#key = '5dad5ab210114bbf98e141921231902'
key = '66228304de824f71a11172133232903'
WEATHER_API_VAR = os.getenv('WEATHER_API')
'''
res = requests.get('http://api.weatherapi.com/v1/current.json?key=5dad5ab210114bbf98e141921231902&q=Glasgo')
print(res.text)
'''
@app.route('/')
def home():
    # return '<h4>Вот твоя переменная = '+str(WEATHER_API_VAR)+'</h4>'
    return '<h1>Домашная работа №1</h1><h3>Получение прогноза - /forecast</h3><h3>Получение текущей погоды - /current</h3>'
@app.route('/forecast/city=<city>&dt=<dt>')
#data  = yyyy-MM-dd
def forecast(city,dt):
    
    today = date.today()
    re_dt= dt.split('-')
    re_dt[1] = re.sub(r'0\d', re_dt[1][1], re_dt[1])
    re_dt[2] = re.sub(r'0\d', re_dt[2][1], re_dt[1])
    diff = (date(int(re_dt[0]),int(re_dt[1]),int(re_dt[2])) - today).days
    #between 14 and 365 days from the current day
    if diff >13 and diff<366:
        space = 'future'
    # less 14 days
    else:
        space = 'forecast'    
   #if date.today() date.
    data = requests.get(WEATHER_API_VAR+space+'.json?key='+key+'&q='+city+'&dt='+dt).text
    country = re.search(r'"country":"[a-zA-Z -]*",',data).group(0)
    city_req = '"city":"'+re.search(r'(?<="name":")[a-zA-Z -]*",',data).group(0)
    avgtemp_c = '"avg_temp":'+re.search(r'(?<="avgtemp_c":)-?\d*.?\d*',data).group(0)+','
    mintemp_c = '"min_temp":'+re.search(r'(?<="mintemp_c":)-?\d*.?\d*',data).group(0)+','
    maxtemp_c = '"max_temp":'+re.search(r'(?<="maxtemp_c":)-?\d*.?\d*',data).group(0)
    res = '{'+country+city_req+avgtemp_c+mintemp_c+maxtemp_c+'}'
    return eval(res)
@app.route('/current/city=<city>')
def current(city):
    data = requests.get(WEATHER_API_VAR+'current.json?key='+key+'&q='+city).text
    country = re.search(r'"country":"[a-zA-Z -]*",',data).group(0)
    city_req = '"city":"'+re.search(r'(?<="name":")[a-zA-Z -]*",',data).group(0)
    temp_c = '"temp_c":'+re.search(r'(?<="temp_c":)-?\d*.?\d*',data).group(0)+','
    res = '{'+country+city_req+temp_c+'}'
    return eval(res)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
