from db import db


class OrderDetailModel(db.Model):
    __tablename__ = 'OrderDetail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shopOrderID = db.Column(db.Integer, db.ForeignKey('ShopOrder.id'))
    shopproductId = db.Column(db.Integer, db.ForeignKey('ShopProduct.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)  # Consider using Decimal or Float for price

    # Relationships
    shop_order = db.relationship('ShopOrderModel', back_populates='order_details')
    shop_product = db.relationship('ShopProductModel', back_populates='order_details')

    def __repr__(self):
        return f"<OrderDetail(id={self.id}, quantity={self.quantity}, price={self.price})>"