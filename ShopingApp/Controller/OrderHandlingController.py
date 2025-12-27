from flask import request,jsonify

from ShopingApp.Model.OrderDetail import OrderDetail
from ShopingApp.Model.OrderModel import OrderModel
from ShopingApp.db import db
from ShopingApp.Model.ProdcutModel import Product
class OrderHandling:
    @staticmethod
    def GetallProducts():
        products = Product.query.all()
        prod=[]
        if products:
            for p in products:
                prod.append({"id":p.id,"name":p.name, "price":p.price})
            return jsonify(prod),200
        return jsonify("no product found"),404

    @staticmethod
    def GetallOrders():
        orders = OrderModel.query.all()
        order=[]
        if orders:
            for o in orders:
                order.append({"id":o.id, "price":o.total_price})
            return jsonify(order),200
        return jsonify("no order found"),404

    @staticmethod
    def GetOrderDetailForId():
        id = request.get_json()
        id = id["id"]
        orderDetails=[]
        orderdetail = OrderDetail.query.filter(OrderDetail.o_id== id).all()
        if orderdetail:
            for od in orderdetail:
                prod = Product.query.filter(Product.id == od.p_id).first()
                orderDetails.append({
                        "Name":prod.name,
                        "Price":prod.price,
                    })
            return jsonify(orderDetails4),200
        return jsonify("no order found"),404

    @staticmethod
    def AddOrder():
        data=request.get_json()
        for d in data:
            newOrder=OrderModel(total_price=data[d]["price"])
            db.session.add(newOrder)
            db.session.commit()
            order_id = newOrder.id

