from extensions import db


class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id
        }


    def __repr__(self):
        return f'<Recipe name={self.name} description={self.email}'