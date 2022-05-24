from os import abort
from flask import Flask, jsonify,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sys



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
    description_body = request.get_json()['description']
    error = True
    body={}
    try:
        new_todo = Todo(description=description_body)
        db.session.add(new_todo)
        body['description'] = new_todo.description
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        abort(500)
    else:
        return jsonify(body)  
    
    db.session.close()
    return redirect(url_for('index'))
    


@app.route('/')
def index():
    return render_template('index.html',data=Todo.query.all())


    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=3000)