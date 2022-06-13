from extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50),unique=True,nullable=False)
    email= db.Column(db.String(50),nullable=False)
    created_at= db.Column(db.DateTime(),server_default=db.func.now())
    status = db.Column(db.Boolean)
    password = db.Column(db.String)
    recipes = db.relationship('Recipe',backref='user',lazy=True)


    def __repr__(self):
        return f'<user name={self.name} email={self.email}'

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        }
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    
    def delete(self):
        db.session.delete(self)
        db.commit()

    @classmethod
    def find_by_name(cls, name):
        user = cls.query.filter(cls.name == name).first()
        return user

    @classmethod
    def find_by_email(cls,email):
        user = cls.query.filter(cls.email == email).first()
        return user

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()