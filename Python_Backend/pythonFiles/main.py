from flask import Flask,json
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import pandas as pd
import math

app = Flask(__name__)
database = 'info_integration' 
username = 'root' 
password = 'mysql' 

# insert into uni_data(ranking,title,country,city,students,stu_staff_rt,intl_stu,gen_rt) values(1,'Trial','trial','trial',100,10.5,10.5,'2:2:30');



CORS(app)
@app.route('/home',methods=['GET'])
def getData():
    extract_load()
    conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_data')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

@app.route('/home/stuData',methods=['GET'])
def getStuData():
    return "Data!"

def extract_load():
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


if __name__ == '__main__':
    app.run(debug=True)