from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# # testing endpoint
# class TestingClass(Resource):
#     def get(self):
#         data = "testing message"
#         return data
# api.add_resource(TestingClass, '/test_endpoint')

# adding this line for db migrate and upgrate
from models import *

from endpoints import *

api.add_resource(TestingClass, '/test_endpoint')

if __name__ == '__main__':
    app.run()