from random import lognormvariate
from types import LambdaType
from flask import Flask,json
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import pandas as pd
import requests
import time
from datetime import datetime, timezone
from opencage.geocoder import OpenCageGeocode

app = Flask(__name__)
databaseTask1 = 'info_integration_task1' 
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
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM uni_data')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    except Error as e:
        print("SQL Error: "+str(e))
        return None
    conn.close()
    return json.dumps(json_data)

@app.route('/weather',methods=['GET'])
def getWeatherData():
    # extract_load_uni_Data()
    json_data=[]
    try:
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM weather')
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        rv = cursor.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
    except Error as e:
        print("SQL Error: "+str(e))
        return None
    conn.close()
    return json.dumps(json_data)

@app.route('/home/stuData',methods=['GET'])
def getStuData():
    return "Data!"

def extract_load_uni_Data(filename):
    try:
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        
        if conn.is_connected():
            cursor = conn.cursor()
            if(filename == "universities_ranking.csv"):
                uniData = pd.read_csv(filename, delimiter = ',',error_bad_lines=False)
                uniData.head()
                for i,row in uniData.iterrows():
                    # row[0] = int(row[0])
                    row[6] = str(row[6])
                    if row[6]=='nan': row[6] = ""
                    # row[4] = row[4].replace("\"","")
                    row[3] = row[3].replace(",","")
                    try:
                        row[5] = row[5].replace("%","")
                        # if(row[6] != ""):
                        #     row[6] = float(row[6])
                    except:
                        print(row)

                    query = "insert into uni_rank_2021(ranking,title,location,num_st,stu_stf_rt,int_st,gender_rt) values(%s,%s,%s,%s,%s,%s,%s)"
                    try:
                        cursor.execute(query,tuple(row))
                    except Error as e:
                        print("Record Insertion failed for: "+ str(row[0]) + " with error: "+ str(e))
                    conn.commit()
            elif(filename == "2020-QS-World-University-Rankings.csv"):
                uniData = pd.read_csv(filename, delimiter = ',',error_bad_lines=False)
                uniData.head()
                for i,row in uniData.iterrows():
                    row = [str(sub).replace('+', '') for sub in row]
                    # row = [str(sub).replace(' ', '') for sub in row]
                    row = [str(sub).replace('=', '') for sub in row]
                    if row[9]=='nan' or row[9]=='-': row[9] = "0"
                    if row[10]=='nan' or row[10]=='-': row[10] = "0"
                    if row[11]=='nan' or row[11]=='-': row[11] = "0"
                    if row[12]=='nan' or row[12]=='-': row[12] = "0"
                    if row[13]=='nan' or row[13]=='-': row[13] = "0"
                    if row[14]=='nan' or row[14]=='-': row[14] = "0"
                    if row[15]=='nan' or row[15]=='-': row[15] = "0"
                    if row[16]=='nan' or row[16]=='-': row[16] = "0"
                    if row[17]=='nan' or row[17]=='-': row[17] = "0"
                    if row[18]=='nan' or row[18]=='-': row[18] = "0"
                    if row[19]=='nan' or row[19]=='-': row[19] = "0"
                    if row[20]=='nan' or row[20]=='-': row[20] = "0"
                    if row[21]=='nan' or row[21]=='-': row[21] = "0"
                    # if('-' in row[9] and len(row[9]) > 2):
                    #     temp_row = row[9].split('-')
                    #     row[9] = (float(temp_row[0]) + float(temp_row[1])) / 2
                    # if('-' in row[10] and len(row[10]) > 2):
                    #     temp_row = row[10].split('-')
                    #     row[10] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[11] and len(row[11]) > 2):
                    #     temp_row = row[11].split('-')
                    #     row[11] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[12] and len(row[12]) > 2):
                    #     temp_row = row[12].split('-')
                    #     row[12] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[13] and len(row[13]) > 2):
                    #     temp_row = row[13].split('-')
                    #     row[13] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[14] and len(row[14]) > 2):
                    #     temp_row = row[14].split('-')
                    #     row[14] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[15] and len(row[15]) > 2):
                    #     temp_row = row[15].split('-')
                    #     row[15] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[16] and len(row[16]) > 2):
                    #     temp_row = row[16].split('-')
                    #     row[16] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[17] and len(row[17]) > 2):
                    #     temp_row = row[17].split('-')
                    #     row[17] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[18] and len(row[18]) > 2):
                    #     temp_row = row[18].split('-')
                    #     row[18] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[19] and len(row[19]) > 2):
                    #     temp_row = row[19].split('-')
                    #     row[19] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    # if('-' in row[20] and len(row[20]) > 2):
                    #     temp_row = row[20].split('-')
                    #     row[20] = (int(temp_row[0]) + int(temp_row[1])) / 2
                    if('-' in row[21] and len(row[21]) > 2):
                        temp_row = row[21].split('-')
                        row[21] = (float(temp_row[0]) + float(temp_row[1])) / 2
                    if('-' in row[0] and len(row[0]) > 2):
                        temp_row = row[0].split('-')
                        row[0] = (float(temp_row[0]) + float(temp_row[1])) / 2
                    if('-' in row[1] and len(row[1]) > 2):
                        temp_row = row[1].split('-')
                        row[1] = (float(temp_row[0]) + float(temp_row[1])) / 2
                    temp_row = [row[0],row[1],row[2],row[3],row[4],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],float(row[17]),float(row[18]),row[19],row[20],row[21]]
                    query = "insert into uni_qs_rank_19_20(rank_in_2020 ,rank_in_2019, institution_name, country, size, status,academic_rep_sc, academic_rep_rk , emp_rep_sc ,emp_rep_rk,faculty_stu_sc ,faculty_stu_rk,citation_fac_sc,citation_fac_rk,intl_fac_sc,intl_fac_rk,intl_stu_sc,intl_stu_rk,overall_score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    try:
                        cursor.execute(query,tuple(temp_row))
                    except Error as e:
                        print("Record Insertion failed for: "+ str(temp_row) + "ROW 18" + str(row[18]) + " with error: "+ str(e))
                    conn.commit()
            else:
                uniData = pd.read_excel(filename)
                uniData.head()
                # uniData.to_sql(name='uni_world_rank_19_20', con=conn)
                for i,row in uniData.iterrows():
                    row[8] = float(row[8])
                    temp_row = [row[0],row[1],row[2],row[8]]
                    query = "insert into uni_world_rank_19_20(world_rank,institution,location,score) values(%s,%s,%s,%s)"
                    try:
                        cursor.execute(query,tuple(temp_row))
                    except Error as e:
                        print("Record Insertion failed for: "+ str(row[0]) + " with error: "+ str(e))
                conn.commit()
        conn.close()
    except Error as e:
        print(str(e))

def getCityData():
    json_data=[]
    try:
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT distinct(city) FROM uni_data where ranking BETWEEN 951 AND 1000')
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
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        cursor = conn.cursor()
        query = "insert into weather(country_code,city,latitude,longitude,date,max_temp,min_temp,curr_temp,pressure,humidity,wind) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,tuple(weather))
        conn.commit()
        conn.close()
    except Error as e:
        print("Record Insertion failed with error: "+ str(e))
        return None
    return 1

def loadTopologicalData():
    key = 'e620de135ddb428da4af8af1eb9a5569'
    try:
        geocoder = OpenCageGeocode(key)
        conn = mysql.connector.connect(host='localhost',database=databaseTask1,user=username,password=password)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sample limit 1569,31')   #check from 1568
        rv = cursor.fetchall()
        for sqlresult in rv:
            results = geocoder.geocode(sqlresult[1])
            queryinput = ()
            if results and len(results):
                aqi = 0
                city = ""
                state = ""
                currency = ""
                if 'city' in results[0]["components"]:
                    city = results[0]["components"]['city']
                if 'state' in results[0]["components"]:
                    state = results[0]["components"]["state"]
                if 'currency' in results[0]["annotations"]:
                    currency = results[0]["annotations"]["currency"]["iso_code"]
                queryinput = (sqlresult[0],aqi,results[0]["geometry"]["lat"],results[0]["geometry"]["lng"],currency,
                    results[0]['annotations']["geohash"],results[0]['annotations']["roadinfo"]["drive_on"],results[0]['annotations']["roadinfo"]["speed_in"],
                    results[0]['annotations']["timezone"]["short_name"],results[0]['annotations']["what3words"]["words"],city,state
                    ,results[0]["formatted"])
                print(queryinput)
                query = "insert into topological_info(uni_fk,aqi,latitude,longitude,currency,geohash,drive_in,speed_in,timezone,what3words,city,state,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query,tuple(queryinput))
                conn.commit()
            else:
                print("NO OUTPUT for University: "+sqlresult[1])
                topo_dump = (sqlresult[0],sqlresult[1])
                query = "insert into topological_dump(uni_fk,institution) values(%s,%s)"
                cursor.execute(query,tuple(topo_dump))
                conn.commit()
            # break
    except Error as e:
        print("Error in loadTopologicalData: "+str(e))
        pass
    conn.close()

if __name__ == '__main__':
    # weather_info()
    # extract_load_uni_Data("2020-QS-World-University-Rankings.csv")
    loadTopologicalData()
    app.run(debug=True)