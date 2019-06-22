# Import Dependencies
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Intitialize Application
app = Flask(__name__)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Create Item Model
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True)
  qty = db.Column(db.Integer)
  measurement = db.Column(db.String(20))

  def __init__(self, name, qty, measurement):
    self.name = name
    self.qty = qty
    self.measurement = measurement

# Item Schema
class ItemSchema(ma.Schema):
  class Meta:
    # Fields to Expose
    fields = ('id', 'name', 'qty', 'measurement')

# Initialize Item Schema
item_schema = ItemSchema(strict=True)
items_schema = ItemSchema(many=True, strict=True)

# GET /
@app.route('/')
def index():
  return 'Hey, There!'

# POST & GET /api/items
@app.route('/api/items', methods=['POST', 'GET'])
def items():
  if request.method == 'POST':

    name = request.json['name']
    qty = request.json['qty']
    measurement = request.json['measurement']
    new_item = Item(name, qty, measurement)

    try:
      db.session.add(new_item)
      db.session.commit()
      return item_schema.jsonify(new_item)
    except: 'There was a problem adding your item'

  else:
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result.data)

# GET /items/<id>
@app.route('/api/items/<id>', methods=['GET', 'PUT', 'DELETE'])
def items_by_id(id):
  item = Item.query.get(id)

  if request.method == 'DELETE':
    try:
      db.session.delete(item)
      db.session.commit()
    except: 'Sorry, we could not delete the item.'

  elif request.method == 'PUT':
    name = request.json['name']
    qty = request.json['qty']
    measurement = request.json['measurement']

    item.name = name
    item.qty = qty
    item.measurement = measurement

    try:
      db.session.commit()
    except:
      return 'Sorry, we could not update the item.'
  
  return item_schema.jsonify(item)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
