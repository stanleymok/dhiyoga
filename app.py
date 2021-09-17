import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# product class/model
class Product(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

ma = Marshmallow(app)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'price')

# init Schema
product_schema = ProductSchema(strict=True)
#products_schema = ProductSchema(strict=True, many=True) #array of products

@app.route('/', methods=['GET'])
def get():
    return jsonify({'dev0': 'Stanley Mok',
                    'dev1': 'Sophia Simangan'})

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    new_product = Product(name, price)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
