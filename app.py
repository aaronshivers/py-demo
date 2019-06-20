# Import Dependencies
from flask import Flask

# Intitialize Application
app = Flask(__name__)

# GET /
@app.route('/')
def index():
  return 'Hey, There!'

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
