# Import Dependencies
from flask import Flask
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

# Create List Model
class List(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True)
  qty = db.Column(db.Integer)
  measurement = db.Column(db.String(20))

  def __init__(self, name, qty, measurement):
    self.name = name
    self.qty = qty
    self.measurement = measurement

# List Schema
class ListSchema(ma.Schema):
  class Meta:
    # Fields to Expose
    fields = ('id', 'name', 'qty', 'measurement')


# GET /
@app.route('/')
def index():
  return 'Hey, There!'

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
