from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://codewarsfx@localhost:5432/codewarsfx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migration = Migrate(app, db)
class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    completed = db.Column(db.Boolean,nullable=False,default=False)

    def __repr__(self):
        return f'<Person id: {self.id} name: {self.name}>'


# db.create_all()
@app.route('/')
#handler function 
def index():
    person = Person.query.first()
    return f'hello {person.name}'