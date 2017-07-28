from flask import Flask
import os

app = Flask(__name__)

# upload path is relative to the directory the app starts in
UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = 1
app.secret_key = 'test key'

path = os.path.dirname(os.path.realpath(__file__))
database_path = os.path.join(path, '../mydb.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
