from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Name', db.String())
    date = db.Column('Date', db.Date)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())
    link = db.Column('Link', db.String())

    def __repr__(self):
        return f'''< Project: (
            id = {self.id}
            name = {self.name}
            date = {self.date}
            description = {self.description}
            skills = {self.skills}
            link = {self.link}
        )'''