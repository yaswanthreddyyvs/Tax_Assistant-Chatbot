from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils.responses import get_response

app = Flask(__name__)
CORS(app)  # Allows the frontend to talk to the backend

# Route to serve the webpage
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle chat messages
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get the user’s message
    user_input = data.get("message", "")
    response = get_response(user_input)  # Get the bot’s answer
    return jsonify({"reply": response})  # Send answer back to frontend

if __name__ == "__main__":
    app.run(debug=True)