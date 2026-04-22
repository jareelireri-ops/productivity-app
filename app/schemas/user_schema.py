from app import ma
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("_password_hash",) # NEVER send the password back to the user

user_schema = UserSchema()