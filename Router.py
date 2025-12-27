from  flask import request,jsonify,Flask
from db import db
app=Flask(__name__)
username='sa'
pwd='123456'
dbinstance='DESKTOP-2GIJV0P\\SUQOON'
db_name='GrocApp'
app.config['SQLALCHEMY_DATABASE_URI']=f'mssql+pyodbc://{username}:{pwd}@{dbinstance}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

@app.route('/')
def Home():
    return jsonify({"message": "Welcome"})
@app.route('/SignUp',methods=['POST'])
def SignUp(username,password,role):
    db.session.query('''select 8 from users''')
    return jsonify({"message": "Welcome"})