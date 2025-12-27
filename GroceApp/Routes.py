from db import db, init_db
from flask import Flask, jsonify
from Model.ShopProductModel import ShopProductModel
from Model.ShopModel import ShopModel
from Model.ShopOrderModel import ShopOrderModel
from Model.OrderDetailModel import OrderDetailModel
from Controller.AccountHandlingController import AccountHandlingController
app = Flask(__name__)
init_db(app)

with app.app_context():
    db.create_all()
    print("created")

@app.route('/')
def welcome():
    return jsonify({"body": "welcome"})
@app.route('/signup',methods=['POST'])
def signup():
    return AccountHandlingController.Signupformobject()
@app.route('/login',methods=['POST'])
def login():
    return AccountHandlingController.Login()
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)