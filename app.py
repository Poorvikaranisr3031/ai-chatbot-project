from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "your name" in user_input:
        return "I am your AI assistant 🤖"
    elif "how are you" in user_input:
        return "I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I am still learning. Please ask something else."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if _name_ == "_main_":
    app.run(debug=True)
