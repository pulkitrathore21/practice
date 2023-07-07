from src import db, ma
from dataclasses import dataclass


@dataclass
class User(db.Model):
    print("start db")
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    add = db.Column(db.String(100), nullable=False)



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        exclude = ["add"]


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
