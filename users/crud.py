from .schemas import User

def create_user(user: User):
    user_dict = user.model_dump()
    print(user)
    return {
        "name": user_dict["username"],
        "email": user_dict["email"]
    }


