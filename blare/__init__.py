import os

from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()

@app.route('/hello')
def hello():
    return '<h1>Hello, World!</h1><p>"{secret}" is the secret!</p><p>"{email}" is the email!</p>'.format(secret=os.getenv('SECRET'), email=os.getenv('EMAIL'))