from flask import request, jsonify
from models import db, User


def register_user_routes(app):

    @app.route("/users", methods=["GET", "POST"])
    def users_collection():
        if request.method == "GET":
            users = db.session.scalars(db.select(User)).all()
            result = [u.serialize() for u in users]
            return jsonify(result)
        elif request.method == "POST":
            data = request.json
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            result = user.serialize()
            return jsonify(result), 201

    @app.route("/users/<int:user_id>", methods=["GET", "DELETE"])
    def user_item(user_id):
        user = db.session.get(User, user_id)
        if not user:
            return {"error": "User not found"}, 404
        if request.method == "GET":
            result = user.serialize()
            return jsonify(result)
        elif request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()
            return "", 204
