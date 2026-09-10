"""
All page routes live here, as a Blueprint.

    /            -> home.html
    /service     -> service.html
    /skills      -> skills.html
    /contact     -> contact.html (GET shows the form, POST sends an email)

app.py only creates the Flask app and registers this blueprint - it has
no route definitions of its own.
"""

from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_mail import Message

from extensions import mail
from config import SITE

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html", site=SITE, active="home")


@main.route("/service")
def service():
    return render_template("service.html", site=SITE, active="service")


@main.route("/skills")
def skills():
    return render_template("skills.html", site=SITE, active="skills")


@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # --- basic server-side validation ---
        if not name or not email or not message:
            flash("Please fill in your name, email and message.", "error")
            return redirect(url_for("main.contact"))

        try:
            msg = Message(
                subject=f"Portfolio contact: {subject or 'New message'}",
                recipients=[current_app.config["MAIL_RECIPIENT"]],
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
            current_app.logger.error("Mail send failed: %s", exc)
            flash(
                "Sorry, something went wrong sending your message. "
                "Please try again later or email me directly.",
                "error",
            )

        return redirect(url_for("main.contact"))

    return render_template("contact.html", site=SITE, active="contact")
