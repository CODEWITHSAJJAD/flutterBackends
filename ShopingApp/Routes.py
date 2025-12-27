from flask import Flask, jsonify

from ShopingApp.Controller.OrderHandlingController import OrderHandling
from ShopingApp.db import db,init_db
from ShopingApp.Model.OrderModel import OrderModel
from ShopingApp.Model.ProdcutModel import Product
from ShopingApp.Model.OrderDetail import OrderDetail
app = Flask(__name__)
init_db(app)
with app.app_context():
    db.create_all()
    print("created")
@app.route('/')
def welcome():
    return jsonify({"body": "welcome"})
@app.route('/getOrders',methods=['GET'])
def order():
    return OrderHandling.GetallOrders()
@app.route('/getProducts',methods=['GET'])
def getProducts():
    return OrderHandling.GetallProducts()
@app.route('/getOrderDetail',methods=['POST'])
def getOrderDetail():
    return OrderHandling.GetOrderDetailForId()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
