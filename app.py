"""
Entry point only. Routes live in routes.py, all settings (including email)
in config.py.
Run with:  python app.py
"""

from flask import Flask

from config import Config
from extensions import mail
from routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)
    app.register_blueprint(main)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
