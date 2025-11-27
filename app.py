# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # New import for CORS
import requests
import os

app = Flask(__name__)

# Enable CORS for all routes and all origins
CORS(app)

# --- CONFIGURATION ---
OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "granite3.3:8b"

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are a helpful and concise Excel formula assistant for financial analysts.
Your responses must be structured into two parts: 'Formula' and 'Explanation'.
Do not provide any conversational text outside of this structure.
If the request is complex, break down the formula into multiple steps.

Example 1:
User: Calculate the average of all values in column C where the value in column B is 'Marketing'.
Formula: =AVERAGEIF(B:B, "Marketing", C:C)
Explanation: This formula calculates the average of values in column C for all rows where the corresponding value in column B is "Marketing".

Example 2 (More Complex):
User: Generate a formula to calculate the Weighted Average Cost of Capital (WACC) given the values are on a sheet named 'WACC_Data'. The values are in cells B2 (Cost of Equity), B3 (Cost of Debt), B4 (Tax Rate), B5 (Market Value of Equity), and B6 (Market Value of Debt).
Formula: =((WACC_Data!B5)/(WACC_Data!B5+WACC_Data!B6)) * WACC_Data!B2 + ((WACC_Data!B6)/(WACC_Data!B5+WACC_Data!B6)) * WACC_Data!B3 * (1 - WACC_Data!B4)
Explanation: This formula calculates WACC by taking the weighted average of the cost of equity and the after-tax cost of debt. It references the given cells on the 'WACC_Data' sheet.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_formula', methods=['POST'])
def generate_formula():
    user_prompt = request.json.get('prompt')
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        
        ollama_response = response.json()
        formula_text = ollama_response['message']['content'].strip()

        return jsonify({"formula": formula_text})

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama: {e}")
        return jsonify({
            "error": f"Failed to connect to Ollama. Please ensure it is running and the model '{MODEL_NAME}' is pulled. Details: {e}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)