## Excel-Formula-Assistant
That's a great final step\! A clear **`README.md`** file is essential for your project. It explains what your Excel Formula AI Assistant does, how to set it up, and how to run it.

Here is a complete `README.md` file using Markdown format.

markdown
#Excel Formula AI Assistant

A full-stack application that uses a local Large Language Model (LLM) powered by **Ollama** to generate complex Excel formulas and provide clear explanations based on natural language input.

## Features

* **AI-Powered Formulas**: Generates correct Excel/Google Sheets formulas from simple English descriptions.
* **Detailed Explanations**: Provides a step-by-step breakdown of how the generated formula works.
* **Clean Chat Interface**: A modern, responsive web chat interface built with HTML, CSS, and JavaScript.
* **Theming**: Supports both Light and Dark modes.
* **Local LLM Integration**: Runs entirely using local resources (Flask and Ollama), ensuring privacy and speed.

## Prerequisites

Before you start, you must have the following installed on your system:

1.  **Python 3.x**
2.  **pip** (Python package installer)
3.  **Ollama**: Download and install the Ollama application.
4.  **Model**: Pull the required model using the Ollama command line.

    **bash**
    ollama pull granite3.3:8b
    

### Setup and Installation

Follow these steps to get your Excel Formula AI Assistant running.

### 1. Project Structure

Ensure your project files are organized correctly:

Excel Formula AI Assistant/
├── app.py
└── templates/
└── index.html


### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies:

**bash**
### Create the environment
python3 -m venv .venv

### Activate the environment (Mac/Linux)
source .venv/bin/activate

### Activate the environment (Windows - PowerShell)
.venv\Scripts\Activate


### 3. Install Python Dependencies

Install all necessary libraries within your active virtual environment:

**bash**
pip install flask flask-cors requests beautifulsoup4


*(Note: The previous versions of this project used `yfinance` and other libraries, which are not needed for the Excel Formula Generator, simplifying the dependencies.)*

### Configuration (app.py)

The application uses port **`5000`** for the Flask server and port **`11434`** for the Ollama API. These are set in your `app.py` file.

The `SYSTEM_PROMPT` in your `app.py` is crucial for guiding the LLM to output correct Excel formulas.

### Running the Application

You will need **two separate terminals** running concurrently.

### Terminal 1: Start Ollama

Start the Ollama server to handle the AI requests:

**bash**
ollama serve

*(Leave this terminal running. If you see an "address already in use" error, it means Ollama is already running in the background.)*

### Terminal 2: Start the Flask App

In your second terminal (with your virtual environment activated), start the Flask web server:

**bash**
python app.py


You should see output indicating the server is running on `http://127.0.0.1:5000/`.

### Usage

1.  Open your web browser and navigate to: **`http://localhost:5000/`**
2.  Type a request into the chat box, such as:
    > "Write a formula to calculate the sum of Column A, but only for rows where Column B contains the word 'Completed'."
3.  The application will send the prompt to the local LLM, and the AI's response (including the formula and explanation) will appear in the chat.
4.  Use the **Copy button** to quickly grab the formula.

## Example Output

The AI's response is structured to be easily parsed by the frontend:

Formula: =SUMIF(B:B, "Completed", A:A)

Explanation: The SUMIF function checks the criteria (the word "Completed") within the range (Column B) and sums the corresponding values in the sum_range (Column A).

