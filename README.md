# Sales Product Recommendation API using Azure OpenAI and Flask

## Overview

This project is a Flask-based API that integrates with Azure OpenAI GPT-4 to recommend suitable financial products (such as loans, credit cards, insurance, etc.) based on customer details. The API takes customer information as input and uses the GPT-4 model to predict which product would best suit the customer.

## Features

- **Customer Data Input**: Accepts customer details (e.g., age, income, credit score).
- **Sales Product Recommendation**: Uses Azure OpenAI's GPT-4 model to recommend a sales product.
- **RESTful API**: A Flask-based API that returns recommendations based on the input provided.

## Technologies Used

- **Flask**: Web framework for Python
- **Azure OpenAI**: For interacting with the GPT-4 model
- **Python**: Backend programming language
- **Azure**: Cloud platform for deploying the model

## Setup and Installation

### Prerequisites

- Python 3.x
- Azure OpenAI API key and endpoint
- A virtual environment (recommended)

### Step 1: Clone the Repository

Clone the repository from your preferred source control and navigate to the project directory.

### Step 2: Set up Environment Variables

Create a `.env` file in the root directory and add your Azure OpenAI credentials, including the `OPENAI_API_KEY` and `OPENAI_API_ENDPOINT`.

### Step 3: Install Dependencies

Install all required dependencies using a package manager like `pip`.

### Step 4: Run the Flask Application

Once the dependencies are installed, run the Flask development server to interact with the API locally.

## API Endpoints

- **POST /recommend-product**: Accepts customer data and returns a sales product recommendation based on the customer’s profile.

## Example Request

The API expects JSON input containing customer details such as name, age, location, credit score, income, etc.

## License

This project is licensed under the MIT License.

