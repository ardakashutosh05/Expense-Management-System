from flask import Flask
from flask_cors import CORS
from routes.expenses import expenses_bp

app = Flask(__name__)
CORS(app)

# Register route
app.register_blueprint(expenses_bp, url_prefix="/api")

@app.route("/")
def home():
    return "Expense Management Backend Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
