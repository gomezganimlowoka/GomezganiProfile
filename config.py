"""
App configuration, loaded from environment variables (see .env.example).
Keeping this separate from app.py and routes.py means credentials and
site content live in one obvious place.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")

    # --- Mail (contact form) ---
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True") == "True"
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL", "False") == "True"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", MAIL_USERNAME)
    # The inbox that should receive contact-form submissions.
    MAIL_RECIPIENT = os.environ.get("MAIL_RECIPIENT", MAIL_USERNAME)


# Site-wide content used across templates (edit this to make it yours).
SITE = {
    "name": "Gomezgani Mlowoka",
    "role": "Software Developer",
    "tagline": "Your IT Presentation Is Our Success Story.",
    "email": "gomezganimlowoka95@gmail.com",
    "handle": "@gomezganimlowoka",
    "bio": (
        "Gomezgani Mlowoka is a Software developer with over 2 years of "
        "experience Machine Learning, Web Development, and Data Science. He has worked on several projects"
    ),
}
