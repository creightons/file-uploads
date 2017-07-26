from flask import Flask

app = Flask(__name__)

# upload path is relative to the directory the app starts in
UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = 1
app.secret_key = 'test key'
