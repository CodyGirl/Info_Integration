from flask import Flask,json
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import pandas as pd
import requests
import time
from datetime import datetime

app = Flask(__name__)
database = 'info_integration' 
username = 'root' 
password = 'mysql'
api_key = 'c1ae9097e6f089ad74f17f63fbd18b9d'
base_url = "http://api.openweathermap.org/data/2.5/weather?q="

CORS(app)
@app.route('/home',methods=['GET'])
def getUniData():
    # extract_load_uni_Data()
    json_data=[]
    try:
        conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM uni_data where ranking BETWEEN 1 AND 50')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    except Error as e:
        print("SQL Error: "+str(e))
        return None
    return json.dumps(json_data)

@app.route('/home/stuData',methods=['GET'])
def getStuData():
    return "Data!"

def extract_load_uni_Data():
    try:
        conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)
        uniData = pd.read_csv("universities_ranking_final.csv", delimiter = ',',error_bad_lines=False)
        uniData.head()
        if conn.is_connected():
            cursor = conn.cursor()
            for i,row in uniData.iterrows():
                row[0] = int(row[0])
                row[7] = str(row[7])
                if row[7]=='nan': row[7] = ""
                row[4] = row[4].replace("\"","")
                row[4] = int(row[4].replace(",",""))
                try:
                    row[6] = row[6].replace("%","")
                    if(row[6] != ""):
                        row[6] = float(row[6])
                except:
                    print(row)

                query = "insert into uni_data(ranking,title,country,city,students,stu_staff_rt,intl_stu,gen_rt) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                try:
                    cursor.execute(query,tuple(row))
                except Error as e:
                    print("Record Insertion failed for: "+ str(row[0]) + " with error: "+ str(e))
                conn.commit()
        conn.close()
    except:
        print({}).format(e)

def getCityData():
    json_data=[]
    try:
        conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT distinct(city) FROM uni_data where ranking BETWEEN 951 AND 100')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    except Error as e:
        print("SQL Error: "+str(e))
        return None
    return json.dumps(json_data)

def weather_info():
    city_data = json.loads(getCityData())
    cities = []
    for i in city_data:
        cities.append(i["city"])
    print("Number of cities in the data source: " + str(len(cities)))

    if (len(cities) > 0):
        for i in cities:
            complete_url = base_url+i+"&appid="+api_key
            print(complete_url)

            # api response
            response = requests.get(complete_url)
            json_response = response.json()

            if(json_response["cod"]!=404):
                weather = parse_city_weather(json_response)
                db_op = insert_weather_data(weather)

def parse_city_weather(weather_json):
    weather = []
    try:
        weather.append(weather_json["sys"]["country"])
        weather.append(weather_json["name"])
        weather.append(weather_json["coord"]["lat"])
        weather.append(weather_json["coord"]["lon"])
        weather.append(datetime.fromtimestamp(weather_json["dt"]).strftime('%d-%m-%y'))
        weather.append(weather_json["main"]["temp_max"])
        weather.append(weather_json["main"]["temp_min"])
        weather.append(weather_json["main"]["temp"])
        weather.append(weather_json["main"]["pressure"])
        weather.append(weather_json["main"]["humidity"])
        weather.append(weather_json["wind"]["speed"])
    except:
        print("Exception while parsing weather object")
    return weather

def insert_weather_data(weather):
    try:
        conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)
        cursor = conn.cursor()
        query = "insert into weather(country_code,city,latitude,longitude,date,max_temp,min_temp,curr_temp,pressure,humidity,wind) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,tuple(weather))
        conn.commit()
        conn.close()
    except Error as e:
        print("Record Insertion failed with error: "+ str(e))
        return None
    return 1

if __name__ == '__main__':
    weather_info()
    app.run(debug=True)