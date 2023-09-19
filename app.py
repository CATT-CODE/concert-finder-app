from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concerts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

API_BASE = "https://www.eventbriteapi.com/v3"
EB_AUTH_TOKEN = os.environ.get('EVENTBRITE_API_TOKEN')

if __name__ == '__main__':
    app.run(debug=True)