from app_blog.extensions import db, ma


class User(db.Model):
    """ User Model for storing user related details """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User id={self.id} email={self.email} username={self.username}>"


class UserSchema(ma.SQLAlchemyAutoSchema):
    model = User
    # include_fk = True хз что это


user_schema = UserSchema()
users_schema = UserSchema(many=True)
