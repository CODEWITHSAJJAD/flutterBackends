from db import  db
class ShopModel(db.Model):
    __tablename__ = 'Shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userAccountName = db.Column(db.String(20), db.ForeignKey('UserAccount.userName'))
    name = db.Column(db.String(20))

    # Relationships
    user_account = db.relationship('UserAccountModel', back_populates='shops')
    shop_products = db.relationship('ShopProductModel', back_populates='shop')
    shop_orders =db.relationship('ShopOrderModel', back_populates='shop')

    def __repr__(self):
        return f"<Shop(id={self.id}, name='{self.name}', userAccountName='{self.userAccountName}')>"

