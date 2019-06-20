# py_demo

## Setup

### Install pipenv
```
sudo apt install pipenv
```

### Start Virtual Environment
```
pipenv shell
```

### Install Dependencies
```
pipenv install
```

### Create Database
```
python
from app import db
db.create_all()
exit()
```

### Run Server - http://localhost:5000
```
python app.py
```