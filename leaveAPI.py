import  pyodbc as pc
from flask import Flask,request,jsonify
app=Flask(__name__)
def connection():
    return pc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=DESKTOP-2GIJV0P\SUQOON;'
            r'DATABASE=LeavesManagement;'
            r'UID=sa;PWD=123456'
    )
@app.route('/InsertLeaves',methods=['POST'])
def leaveInsert():
    data = request.get_json()
    date=data['date']
    title=data['title']
    student_name=data['student_name']
    comments=data['comments']
    teacher_name=data['teacher_name']
    type=data['type']
    isApproved=data['isApproved']
    conn = connection()
    cursor = conn.cursor()
    query = "INSERT INTO Leave (L_date,title, student_name, comments,teacher_name,l_type,isApproved) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(query, (date, title, student_name,comments,teacher_name,type,isApproved))
    cursor.commit()
    cursor.close()
    conn.close()
    return jsonify({"message":"Leave inserted"}),201

@app.route('/getLeaves',methods=['GET'])
def Leave_get():
    conn = connection()
    cursor = conn.cursor()
    selquery = "select * from Leave"
    data = cursor.execute(selquery).fetchall()
    columns = [desc[0] for desc in cursor.description]
    allLeaves = []
    for row in data:
        row_dict = dict(zip(columns, row))
        allLeaves.append({
            "date": row_dict['L_date'],
            "title": row_dict['title'],
            "student_name": row_dict['student_name'],
            "comments": row_dict['comments'],
            "teacher_name": row_dict['teacher_name'],
            "type": row_dict['l_type'],
            "isApproved": row_dict['isApproved'],
        })

    print(allLeaves)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(allLeaves)
@app.route('/login',methods=['POST'])
def login():
    con=connection()
    data=request.get_json()
    usr=data['username']
    pwd=data['pwd']
    selquery=''''select role from user where username=? and password=?'''
    cursor=con.cursor()
    result=cursor.execute(selquery,(usr,pwd)).fetchone()
    cursor.close()
    con.close()
    if result:
        return jsonify(result),200
    return jsonify("invalid username or password")

if __name__=="__main__":
    app.run(port=2020,debug=True)