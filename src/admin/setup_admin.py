import os
from flask_admin import Admin
from models import db, User, Planet, Character, FavoritePlanet, FavoriteCharacter
from admin.model_wrapper import StandardModelView


def setup_admin(app):
    app.secret_key = os.environ.get("FLASK_APP_KEY", "sample key")
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"

    admin = Admin(app, name="4Geeks Admin", template_mode="bootstrap3")

    with app.app_context():
        admin.add_view(StandardModelView(User, db.session))
        admin.add_view(StandardModelView(Planet, db.session))
        admin.add_view(StandardModelView(Character, db.session))
        admin.add_view(StandardModelView(FavoritePlanet, db.session))
        admin.add_view(StandardModelView(FavoriteCharacter, db.session))
