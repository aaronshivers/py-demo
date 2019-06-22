# py_demo

## Setup

### Clone Repository
```
git clone git@github.com:aaronshivers/py-demo.git
```

### Move into the Project Directory
```
cd py-demo
```


### Start Virtual Environment
```
pipenv shell
```

### Install pipenv
```
sudo apt install pipenv
```

### Install Dependencies
```
pipenv install
```

### Create Database
```
python3
from app import db
db.create_all()
exit()
```

### Run Server - (http://localhost:5000)
```
python3 app.py
```
