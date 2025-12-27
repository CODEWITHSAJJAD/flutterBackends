import pyodbc
from flask import jsonify,request,Flask
def con():
    return pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-2GIJV0P\SUQOON;'
    r'DATABASE=GrocApp;'
    r'UID=sa;PWD=123456'
    )

def signup():
    data1=request.get_data()
    data=request.get_json()
    usr=data['username']
    pwd=data['password']
    rl=data['role']

    conn = con()
    cursor=conn.cursor()
    selquery = "select * from users where username=?"
    users = cursor.execute(selquery,usr).fetchone()
    if users[0]==usr:
        message='user name already registered'
        conn.commit()
        conn.close()
        return  jsonify({
        "message": message,
    }),403
    else:
        query = "INSERT INTO users (username, password, role,imagepath) VALUES (?,?,?,?)"
        cursor.execute(query,(usr,pwd,rl))
        message = 'Signup success'
        conn.commit()
        conn.close()
        return jsonify({
        "message": message,
    }),200

def login():
    data = request.get_json()
    usr = data['username']
    pwd = data['password']
    if usr and pwd:
        conn = con()
        cursor = conn.cursor()
        selquery = "SELECT * FROMers WHERE username=? us AND password=?"
        users = cursor.execute(selquery, (usr, pwd)).fetchone()
        if users:
            role = users[2]
            return jsonify({"message": role}), 200
        else:
            return jsonify({"message": "invalid"}), 401
    else:
        return jsonify({"message": "invalid"}), 400
