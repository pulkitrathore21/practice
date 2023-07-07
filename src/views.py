from flask import Blueprint, request
from src.models import User, db, user_schemas
from flask import current_app
import logging

user_api = Blueprint("user_api", __name__, url_prefix="/user")


@user_api.route("/", methods=["POST"])
def new_user():
    # username=request.json.get("username")
    # user=User(username=username,email=email,add=add)
    # db.session.add(user)
    # db.session.commit()
    return {"success": True, "message": "user addedd successfully"}, 200


@user_api.route("/all-users", methods=["GET"])
def users():
    print("hii all users")
    result = User.query
    logging.info("admin loggin successfully")
    result = user_schemas.dump(result)
    return {"success": True, "message": result}
