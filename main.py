from flask import Flask  # pyright: ignore[reportMissingImports]

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/service')
def service():
    return "Service Page"

@app.route('/skills')
def skills():
    return "Skills Page" 

@app.route('/contact')
def contact():
    return "Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
