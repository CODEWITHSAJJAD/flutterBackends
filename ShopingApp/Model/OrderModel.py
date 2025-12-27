from ShopingApp.db import db
class OrderModel(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float)

    orderdetail_rl = db.relationship("OrderDetail",back_populates="order_rl")
