"""
Portfolio Flask application.

Routes:
    /            -> home.html
    /service     -> service.html
    /skills      -> skills.html
    /contact     -> contact.html (GET shows the form, POST sends an email)

Email is sent with Flask-Mail. Configure real credentials in a .env file
(see .env.example) before deploying - the app will run without them, but
the contact form will show an error until SMTP is configured.
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Core config
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")

# Mail config
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS", "True") == "True"
app.config["MAIL_USE_SSL"] = os.environ.get("MAIL_USE_SSL", "False") == "True"
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get(
    "MAIL_DEFAULT_SENDER", app.config["MAIL_USERNAME"]
)
# The inbox that should receive contact-form submissions.
app.config["MAIL_RECIPIENT"] = os.environ.get(
    "MAIL_RECIPIENT", app.config["MAIL_USERNAME"]
)

mail = Mail(app)

# Site-wide content used across templates (edit this to make it yours).
SITE = {
    "name": "Gomezgani Mlowoka",
    "role": "Freelance Copy Specialist",
    "tagline": "Words that work as hard as your brand does.",
    "email": "gomezganimlowoka95@gmail.com",
    "handle": "@gomezganimlowoka",
    "bio": (
        "Gomezgani Mlowoka is a software developer with over 2 years of "
        "experience specialising in machine learning, web development, and data analysis. He has a proven track record of "
        "for brands and organisations across Southern Africa."
    ),
}


@app.route("/")
def home():
    return render_template("home.html", site=SITE, active="home")


@app.route("/service")
def service():
    return render_template("service.html", site=SITE, active="service")


@app.route("/skills")
def skills():
    return render_template("skills.html", site=SITE, active="skills")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # --- basic server-side validation ---
        if not name or not email or not message:
            flash("Please fill in your name, email and message.", "error")
            return redirect(url_for("contact"))

        try:
            msg = Message(
                subject=f"Portfolio contact: {subject or 'New message'}",
                recipients=[app.config["MAIL_RECIPIENT"]],
                reply_to=email,
                body=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Subject: {subject}\n\n"
                    f"{message}"
                ),
            )
            mail.send(msg)
            flash("Thanks! Your message has been sent - I'll reply soon.", "success")
        except Exception as exc:  # noqa: BLE001 - show a friendly error either way
            app.logger.error("Mail send failed: %s", exc)
            flash(
                "Sorry, something went wrong sending your message. "
                "Please try again later or email me directly.",
                "error",
            )

        return redirect(url_for("contact"))

    return render_template("contact.html", site=SITE, active="contact")


if __name__ == "__main__":
    app.run(debug=True)
