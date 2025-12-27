from db import  db
class ShopProductModel(db.Model):
    __tablename__ = 'ShopProduct'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shopid = db.Column(db.Integer, db.ForeignKey('Shop.id'))
    name = db.Column(db.String(20))
    price = db.Column(db.String(20))

    # Relationships
    shop = db.relationship('ShopModel', back_populates='shop_products')
    order_details = db.relationship('OrderDetailModel', back_populates='shop_product')

    def __repr__(self):
        return f"<ShopProduct(id={self.id}, name='{self.name}', price='{self.price}')>"
