class Config:
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'postgresql://codewarsfx@localhost:5432/recipes'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY='my name is chidera'