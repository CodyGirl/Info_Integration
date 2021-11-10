from flask import Flask,json
from flask_cors import CORS
import pyodbc
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
database = 'info_integration' 
username = 'root' 
password = 'mysql' 
# conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Sever = DESKTOP-3H5IL08;Database = info_integration;Trusted_Connection=yes;')
# print(pyodbc.drivers())
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-3H5IL08'+';DATABASE='+database+';Trusted_Connection=yes;'+'UID='+username+';PWD='+password+';')

conn = mysql.connector.connect(host='localhost',database=database,user=username,password=password)

CORS(app)
@app.route('/home',methods=['GET'])
def getData():
    
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

if __name__ == '__main__':
    app.run(debug=True)