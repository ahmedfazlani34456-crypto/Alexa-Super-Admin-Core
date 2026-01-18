from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Alexa's Logic for P1
@app.route('/')
def index():
    return render_template('p1_dashboard.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get('command', '').lower()
    command_type = data.get('type', 'text') # voice or text

    # P1 Working Logic (No Popups)
    print(f"[Alexa P1]: Master Admin ka {command_type} command mila: {command}")
    
    # Identity Hide/Masking Action
    if "hide me" in command or "identity" in command:
        response = "MashaAllah Master Admin, aapki identity ab Ghost Mode mein hai."
    else:
        response = "Command received. Alexa is working in background..."

    return jsonify({"status": "Success", "message": response})

if __name__ == "__main__":
    # Port 5001 for P1
    app.run(host='0.0.0.0', port=5001)
