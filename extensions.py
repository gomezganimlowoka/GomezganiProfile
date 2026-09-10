"""
Extension instances live here (not in app.py or routes.py) so both files
can import the same `mail` object without circular imports.
"""

from flask_mail import Mail

mail = Mail()
