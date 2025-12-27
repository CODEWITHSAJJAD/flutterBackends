from ShopingApp.db import db
class OrderDetail(db.Model):
    __tablename__ = 'orderdetail'
    id = db.Column(db.Integer, primary_key=True)
    o_id=db.Column(db.Integer,db.ForeignKey('order.id'))
    p_id=db.Column(db.Integer,db.ForeignKey('product.id'))

    order_rl=db.relationship("OrderModel",back_populates="orderdetail_rl")
    prod_rl=db.relationship("Product",back_populates="orderdetail_rl")
