from db import db
class ShopOrderModel(db.Model):
    __tablename__ = 'ShopOrder'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shopid = db.Column(db.Integer, db.ForeignKey('Shop.id'))
    userAccountName = db.Column(db.String(20), db.ForeignKey('UserAccount.userName'))
    date = db.Column(db.Date)
    status = db.Column(db.Integer)

    # Relationships
    shop = db.relationship('ShopModel', back_populates='shop_orders')
    user_account = db.relationship('UserAccountModel', back_populates='shop_orders')
    order_details = db.relationship('OrderDetailModel', back_populates='shop_order')

    def __repr__(self):
        return f"<ShopOrder(id={self.id}, date={self.date}, status={self.status})>"