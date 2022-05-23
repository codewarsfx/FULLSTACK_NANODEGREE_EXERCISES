from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
db= SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://codewarsfx@localhost:5432/codewarsfx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    description = db.Column(db.String,nullable=False) 


    def __repr__(self):
        return f'<todo id={self.id} description={self.description} >'

db.create_all()

@app.route('/create',methods=['POST'])
def create():
    description_body = request.form.get('description')
    new_todo = Todo(description=description_body)
    db.session.add(new_todo)
    db.session.commit()
    db.session.close()
    return redirect(url_for('index'))
    


@app.route('/')
def index():
    return render_template('index.html',data=Todo.query.all())