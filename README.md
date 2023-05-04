# Welcome to the Flask-skeleton by Sl00x 😁

Flask-Skeleton is a Flask-based Python framework that allows for optimized and rapid creation of RESTful APIs. This documentation will help you better understand how to set up the project without any bugs and ensure that everything runs smoothly from the first launch. A dream come true, isn't it?

### Prerequisites
In first time you need to have Python3.X 🚀 install on your machine
Open the command prompt on your computer.

Type the following command to update the package list:
```sh
sudo apt-get update
```
Next, type the following command to install Python 3:
```sh
sudo apt-get install python3
```
Once the installation is complete, you can verify that Python 3 is installed by typing the following command:
```sh
python3 --version
```
This should display the version of Python 3 that is installed on your system.
Now for mac os version : 
You need tu install *Homebrew* with this command line 
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
In the second time you can install python after the *Hombrew* downloading
```sh
brew install python3
```

You need to have *docker* and *docker-compose* install on your computer
> 🐳 [Docker Redirection documentation](https://hub.docker.com/)

## Start First Run 🔥
Go in you repository **Flask-Sl00x-Skeleton-auth** and for the first time you need to create a virtual environnement for the project
```sh
python3 -m venv env
```
After you run this command you need to active  the virtual env
```sh
source /env/bin/activate
```
if you are usin fish shell 
```sh
source /env/bin/activate.fish
```
After if you want to deactivate the virtual env it's really simple 
```sh
deactivate
```
And to finish the setup virtual env you need to download all the dependency of the project which are in **requirement.txt** file
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

It's not finish now build the docker image now with database and after we setup the **.env** file for the connexion
to build docker it's really simple : 
```sh
docker-compose up -d
```
if you want any information about your containers type this command : 
```sh
docker-compose logs -f <CONTAINER_NAME>
```
all its good but you can't launch your api server because you need to setup the database. For this create .env file 
```sh
touch .env
```
and put this into the file 
```py
DB_HOST=<YOUR_HOST>
DB_PORT=<YOUR_PORT>
DB_USER = <YOUR_USER>
DB_PASSWORD = <YOUR_PASSWORD>
DB_NAME = <YOUR_DATABASE_NAME>

JWT_SECRET_WORD = <YOUR_SECRET_KEY_FOR_JWT>
```

After you can run the project : 
```sh
python3 app.py
```

## Migration ↔

You want to migrate the new version of the database no problem with this template all is configure to make this
```sh
flask db init
```
```sh
flask db update "add User information"
```


## How to create authentication 🔐

Its really simple to create an authentication with this template because is already coded for you
go in your controller 
```sh
cd Controllers || mkdir UserController.py
```

add this code: 
```py
from Models.User import User
from flask import jsonify
from http import HTTPStatus
from database import db
from Authentication.Authentication import Authenticate



class UserController:
    def get_all_users():
        db.create_all()
        try:
            users = User.query.all()
            users_list = []
            for user in users:
                users_list.append(user.serialize())
            return users_list, HTTPStatus.OK
        except  Exception as e:
            return jsonify({"message": "BAD_REQUEST"}), HTTPStatus.BAD_REQUEST

    def authenticate(data):
        try:
            auth = Authenticate(username=data['username'], password=data['password'])
            return auth.auhtenticate()
        except Exception as e:
            return jsonify({"message": "BAD_REQUEST"}), HTTPStatus.BAD_REQUEST
        
```

It's all for this part

