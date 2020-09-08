# Hospital Management System

### Description
- This is an open source graphql server that can be consumed with a front end library like React, Angular , Vue etc to establish a web system that can fully manage a hospital

### Development
This Application is developed using python pure [Flask](http://flask.pocoo.org/docs/1.0/).The data is stored on python data structures



### Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python web microframework)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)
- [Pylint](https://www.pylint.org/) (Linting library)
- [Pip3](https://pypi.org/project/pip/) (Python package installer)

### Graphql
- `http://localhost:5000/graphql`                          

#1## Getting Started with version two:

**To start the app, please follow the instructions below:**

**On your terminal:**

Install pip:
Install
Install sudo apt-get install python-pip
Install
- Clone this repository:

        $ git clone https://github.com/Nduhiu17/hsm-flask-graphene.git

- Get into the root directory:

        $ cd hsm-flask-graphene/

- Install virtual enviroment:

        $ python3.6 -m venv virtual

- Activate the virtual environment:

        $ source virtual/bin/activate
  
- Install requirements

        $ pip install -r requirements.txt

- Create postgress databases by running the following commands:

        $ psql

        $ CREATE DATABASE yourdbname WITH PASSWORD yourpassword

        $ CREATE DATABASE yourtestdbname WITH PASSWORD yourpassword

-Export server's secret key by:

        $ export SECRET_KEY='set-your-secret-key-here'

-Export server's JWT SECRET KEY by:

        $ export JWT_SECRET_KEY='set-your-secret-key-here'

-Export server's DATABASE URL by:

        $ export DATABASE_URL='postgres://yourdbusername:yourdbpassword@localhost:5432/yourdbname'


- Run the server by:

        $ python manage.py server

### Running the tests

-Export server's secret key to the environment by:

        $ export SECRET_KEY='set-your-secret-key-here'

-Export server's JWT SECRET KEY by:

        $ export JWT_SECRET_KEY='set-your-secret-key-here'

-Export test DATABASE URL by:

        $ export DATABASE_URL='postgres://yourdbusername:yourdbpassword@localhost:5432/yourtestdbname'


Run the tests by:

         $ pytest

### Author
Antony Mundia