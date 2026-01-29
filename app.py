from flask import Flask, request, jsonify
from data import college_data

app = Flask(__name__)

def get_intent(message):
    message = message.lower()

    if "admission" in message:
        return "admission"
    elif "course" in message or "department" in message:
        return "courses"
    elif "fee" in message:
        return "fees"
    elif "hostel" in message:
        return "hostel"
    elif "transport" in message or "bus" in message:
        return "transport"
    elif "placement" in message or "job" in message:
        return "placements"
    elif "scholarship" in message:
        return "scholarship"
    elif "time" in message or "timing" in message:
        return "timings"
    elif "contact" in message or "phone" in message:
        return "contact"
    elif "location" in message or "address" in message:
        return "location"
    else:
        return None

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    intent = get_intent(user_message)

    if intent and intent in college_data:
        reply = college_data[intent]
    else:
        reply = "Please contact the college office for detailed information."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
  
