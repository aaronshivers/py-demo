# Import Dependencies
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Intitialize Application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
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

# POST /api/items
@app.route('/api/items', methods=['POST'])
def add_item():
  name = request.json['name']
  qty = request.json['qty']
  measurement = request.json['measurement']

  new_item = Item(name, qty, measurement)

  db.session.add(new_item)
  db.session.commit()

  return item_schema.jsonify(new_item)

# GET /
@app.route('/')
def index():
  return 'Hey, There!'

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
