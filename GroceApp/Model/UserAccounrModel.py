from db import  db
class UserAccountModel(db.Model):
    __tablename__ = 'UserAccount'

    userName = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20))
    profileImagePath = db.Column(db.String(20))
    role = db.Column(db.Integer)  
    city = db.Column(db.String(20))

    # Relationships
    shops = db.relationship('ShopModel', back_populates='user_account')
    shop_orders = db.relationship('ShopOrderModel', back_populates='user_account')

    def __repr__(self):
        return f"<UserAccount(userName='{self.userName}', role={self.role}, city='{self.city}')>"