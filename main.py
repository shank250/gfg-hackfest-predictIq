# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests
# import os

# app = Flask(__name__)
# #  Get the frontend URL from an environment variable, or use a default
# # FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:5001')

# # Configure CORS to allow requests from the frontend URL
# # CORS(app, resources={r"/api/*": {"origins": FRONTEND_URL}})
# CORS(app, resources={r"/*": {"origins": "*"}})
# #
# # Azure OpenAI Configuration

# # Dummy customer data
# dummy_data = {
#     "Customer ID": 1,
#     "Name": "John Smith",
#     "Age": 32,
#     "Location": "San Francisco, CA",
#     "Credit Score": 750,
#     "Has Credit Card": "Yes",
#     "Estimated Salary": "$100,000",
#     "Excited": "Yes",
#     "Tenure": "5 years",
#     "Marital": "Married",
#     "Loan Type": "Car"
# }

# @app.route('/api/recommend', methods=['POST'])
# def recommend_product():
#     user_input = request.json
    
#     # Combine user input with dummy data
#     full_data = {**dummy_data, **user_input}
    
#     # Prepare the payload for Azure OpenAI
#     payload = {
#         "messages": [
#             {
#                 "role": "system",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": "You are a banking analyst. Based on the customer details, suggest the best product to pitch to the user. Be concise and focus on key selling points."
#                     }
#                 ]
#             },
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": str(full_data)
#                     }
#                 ]
#             }
#         ],
#         "temperature": 0.7,
#         "top_p": 0.95,
#         "max_tokens": 800
#     }
    
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": API_KEY,
#     }
    
#     try:
#         response = requests.post(ENDPOINT, headers=headers, json=payload)
#         response.raise_for_status()
#         recommendation = response.json()['choices'][0]['message']['content']
#         return jsonify({"recommendation": recommendation})
#     except requests.RequestException as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import random
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")
# openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

# Multiple dummy customer data profiles
dummy_data_profiles = [
    {
        "Customer ID": 1,
        "Name": "Shivam Kumar",
        "Age": 32,
        "Location": "San Francisco, CA",
        "Credit Score": 750,
        "Has Credit Card": "Yes",
        "Estimated Salary": "$100,000",
        "Excited": "Yes",
        "Tenure": "5 years",
        "Marital": "Married",
        "Loan Type": "Car"
    },
    {
        "Customer ID": 2,
        "Name": "Priya Sharma",
        "Age": 28,
        "Location": "Mumbai, India",
        "Credit Score": 680,
        "Has Credit Card": "No",
        "Estimated Salary": "₹1,500,000",
        "Excited": "No",
        "Tenure": "2 years",
        "Marital": "Single",
        "Loan Type": "Personal"
    },
    {
        "Customer ID": 3,
        "Name": "Alex Johnson",
        "Age": 45,
        "Location": "London, UK",
        "Credit Score": 820,
        "Has Credit Card": "Yes",
        "Estimated Salary": "£80,000",
        "Excited": "Yes",
        "Tenure": "10 years",
        "Marital": "Divorced",
        "Loan Type": "Home"
    }
]

# Special profile for account number 2000
sandip_jain_profile = {
    "Customer ID": 2000,
    "Name": "Sandip Jain",
    "Age": 40,
    "Location": "Delhi, India",
    "Credit Score": 790,
    "Has Credit Card": "Yes",
    "Estimated Salary": "₹5,000,000",
    "Excited": "Yes",
    "Tenure": "8 years",
    "Marital": "Married",
    "Loan Type": "Business"
}

@app.route('/api/recommend', methods=['POST'])
def recommend_product():
    user_input = request.json
    
    account_number = user_input.get("accountNumber", "")
    
    if account_number == 2000:
        selected_profile = sandip_jain_profile
    else:
        selected_profile = random.choice(dummy_data_profiles)
    
    # Use username from input, everything else from selected profile
    full_data = {
        **selected_profile,
        "Name": user_input.get("username", selected_profile["Name"])
    }
    
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a banking analyst. Based on the customer details, suggest the best product to pitch to the user. Be concise and focus on key selling points. Do not use asterisks or other markdown formatting in your response."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": str(full_data)
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        recommendation = response.json()['choices'][0]['message']['content']
        
        # Remove any remaining asterisks
        recommendation = re.sub(r'\*+', '', recommendation)
        
        return jsonify({
            "recommendation": recommendation,
            "profile": full_data  # Include the profile data in the response
        })
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')