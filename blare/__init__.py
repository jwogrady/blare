import os

from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()

@app.route('/hello')
def hello():
    secret = os.getenv('SECRET_KEY')
    email = os.getenv('ADMIN_EMAIL')
    return '<h1>Hello, World!</h1><ul><li>Secret: {secret}</li><li>Email: {email}</li></ul>'.format(
        secret=secret,
        email=email
    )