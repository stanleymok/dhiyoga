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
    header1 = db.Column(db.String(40))
    paragraph1 = db.Column(db.String(1000))

    def __init__(self, header1, paragraph1):
        self.header1 = header1
        self.paragraph1 = paragraph1

ma = Marshmallow(app)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'header1', 'paragraph1')

# init Schema
product_schema = ProductSchema()#strict=True)
#product_schema = ProductSchema(strict=True)
#products_schema = ProductSchema(strict=True, many=True) #array of products

@app.route('/', methods=['GET'])
def get():
    return jsonify({'dev0': 'Stanley Mok',
                    'dev1': 'Sophia Simangan'})

@app.route('/product', methods=['POST'])
def add_product():
    header1 = request.json['header1']
    paragraph1 = request.json['paragraph1']
    new_product = Product(header1, paragraph1)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
