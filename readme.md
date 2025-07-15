-----

# Money Mind Pal: Personal Finance Dashboard & AI Assistant

Money Mind Pal is an interactive web application built with Streamlit designed to help users visualize and understand their financial data. It features a comprehensive dashboard with various charts and a conversational AI chatbot to answer financial questions in natural language.

*(Suggestion: Replace the placeholder above with a screenshot or GIF of your running application.)*

-----

## 📋 Table of Contents

  - [Features](https://www.google.com/search?q=%23-features)
  - [Technologies Used](https://www.google.com/search?q=%23-technologies-used)
  - [Setup and Installation](https://www.google.com/search?q=%23-setup-and-installation)
  - [How to Use](https://www.google.com/search?q=%23-how-to-use)
  - [Project Structure](https://www.google.com/search?q=%23-project-structure)
  - [Future Improvements](https://www.google.com/search?q=%23-future-improvements)

-----

## ✨ Features

This project is composed of two main components: a Financial Dashboard and a Chatbot Assistant.

### 💹 Financial Dashboard (`main.py`)

  - **Interactive Visualizations**: Clean and intuitive charts to explore your financial history.
  - **Withdrawal Analysis**: A horizontal bar chart showing total withdrawal amounts broken down by category.
  - **Trend Tracking**: Line charts displaying total monthly deposits and withdrawals to identify patterns over time.
  - **Spending Distribution**: A pie chart that illustrates the percentage of spending across different categories.
  - **Key Metrics**: At-a-glance summary of total deposit and withdrawal amounts.
  - **Personalized Notifications**: A notification system provides helpful tips and alerts based on spending habits (e.g., spending limit warnings, coffee purchase streaks).

### 🤖 AI Chatbot Assistant (`chatbot.py`)

  - **Conversational Interface**: Ask questions about your financial data using natural language.
  - **OpenAI Integration**: Leverages the power of GPT-3.5-Turbo to understand queries and provide intelligent responses.
  - **Voice-to-Text**: Use your microphone to ask questions with the integrated speech recognition feature.
  - **On-Demand Graphs**: Ask the chatbot to generate and display specific graphs (e.g., "show me a graph of my withdrawals").
  - **Financial Projections**: Includes a predictive feature to forecast future savings based on current habits and inputs.

-----

## 🛠️ Technologies Used

  - **Backend/Framework**: Python, Streamlit
  - **Data Manipulation**: Pandas, NumPy
  - **Data Visualization**: Plotly Express, Matplotlib, Seaborn
  - **AI & NLP**: OpenAI API
  - **Speech Recognition**: SpeechRecognition
  - **Utilities**: subprocess, calendar, json, os

-----

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

**2. Create a Virtual Environment (Recommended)**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
Create a file named `requirements.txt` and add the following libraries to it:

```txt
streamlit
pandas
plotly
openai
matplotlib
seaborn
SpeechRecognition
numpy
```

Then, install them using pip:

```bash
pip install -r requirements.txt
```

*Note: You may also need to install `PyAudio` for the speech recognition feature to work.*

**4. Configure OpenAI API Key**

> **⚠️ Security Warning\!**
> The provided `chatbot.py` file contains a hardcoded OpenAI API key. This is a significant security risk. You should immediately invalidate that key and use a secure method to store your new key.

Open the `chatbot.py` file and replace the hardcoded key with your own. It is highly recommended to use environment variables for this.

**Replace this:**

```python
api_key = "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" # Your hardcoded key
openai.api_key = api_key
```

**With this:**

```python
import os

# Load the key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
```

You would then set the environment variable in your terminal before running the app.

-----

## 🚀 How to Use

**1. Running the Main Dashboard**
To start the main financial dashboard, run the following command in your terminal:

```bash
streamlit run main.py
```

This will open the application in your default web browser.

**2. Using the Chatbot**
The main dashboard has a "Chatbot" button in the sidebar. Clicking it attempts to launch the `chatbot.py` application in a new process.

Alternatively, you can run the chatbot directly from your terminal:

```bash
streamlit run chatbot.py
```

-----

## 📁 Project Structure

Here is the basic file structure for the project:

```
.
├── main.py             # Main Streamlit app for the dashboard
├── chatbot.py          # Streamlit app for the AI assistant
├── myLogo.png          # Logo file used in the dashboard
├── animation_5.gif     # Animation file used in the dashboard
├── requirements.txt    # List of Python dependencies
└── README.md           # This file
```

-----

## 🔮 Future Improvements

  - **Secure API Key Management**: Fully integrate environment variables or a `.env` file for storing the OpenAI API key.
  - **Dynamic Notifications**: Replace the hardcoded dashboard notifications with alerts generated dynamically from the user's data.
  - **Seamless App Integration**: Combine the two Streamlit apps into a single, multi-page application instead of using `subprocess`.
  - **Improved Chatbot Context**: Remove hardcoded chatbot responses and improve its ability to derive all insights directly from the provided financial data.
  - **User Authentication**: Implement a login system to allow multiple users to manage their own financial data securely.
