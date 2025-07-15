-----

# 💰 Money Mind Pal — Personal Finance Dashboard with AI Chat Assistant

Money Mind Pal is an interactive **Streamlit financial dashboard** supercharged with an **AI-powered chatbot assistant**. It's designed to help you visualize spending and saving habits, ask complex questions about your financial data using either text or voice, and receive intelligent, data-driven insights—all derived directly from your transaction history.

This tool transforms a simple transaction spreadsheet into a powerful, interactive financial command center.

-----

## 📋 Table of Contents

  - [Features](https://www.google.com/search?q=%23-features)
  - [Technologies Used](https://www.google.com/search?q=%23-technologies-used)
  - [Project Structure](https://www.google.com/search?q=%23-project-structure)
  - [Setup and Installation](https://www.google.com/search?q=%23-setup-and-installation)
  - [How to Use](https://www.google.com/search?q=%23-how-to-use)
  - [Sample Dataset & Prompts](https://www.google.com/search?q=%23-sample-dataset--prompts)
  - [Screenshots](https://www.google.com/search?q=%23-screenshots)
  - [Future Improvements](https://www.google.com/search?q=%23-future-improvements)
  - [License](https://www.google.com/search?q=%23-license)
  - [Acknowledgements](https://www.google.com/search?q=%23-acknowledgements)

-----

## ✨ Features

This project is composed of two main components: a Financial Dashboard and a Chatbot Assistant.

### 💹 Financial Dashboard (`main.py`)

The main dashboard provides a high-level overview of your financial health through rich, interactive visualizations.

  - **Interactive Visualizations**: Clean and intuitive charts built with Plotly to explore your financial history.
  - **Monthly Financial Summary**: A comparative line chart that displays your total withdrawals versus your total deposits for each month, making it easy to spot months with high spending or high income.
  - **Top Spending Categories**: A dynamic horizontal bar chart that automatically identifies and visualizes your top spending categories, allowing you to instantly see where most of your money is going.
  - **Spending Distribution**: A pie chart that illustrates the percentage of spending across different categories.
  - **Key Metrics**: At-a-glance summary cards for total deposit and withdrawal amounts.
  - **Personalized Notifications**: A custom notification system provides helpful tips and alerts based on spending habits (e.g., spending limit warnings, coffee purchase streaks).
  - **Seamless Chatbot Integration**: A simple button in the sidebar to launch the AI Chatbot assistant.

### 🤖 AI Chatbot Assistant (`chatbot.py`)

The AI assistant allows you to dive deeper into your financial data by asking questions in natural language.

  - **Conversational Interface**: A user-friendly chat interface to ask any question about your finances.
  - **🎙️ Voice-to-Text Input**: Features a "Use Speech to Text" button that lets you ask questions using your microphone, powered by the `speech_recognition` library.
  - **Advanced AI Engine**: Leverages the power of OpenAI's **GPT-3.5-Turbo** model to understand context, analyze your data, and provide insightful, human-like answers.
  - **On-the-Fly Chart Generation**: The chatbot can generate and display charts based on your questions. For example, asking "Show me my withdrawals by month" will render the relevant graph directly in the chat.
  - **Pre-built & Custom Logic**: Includes hardcoded logic for common financial queries to provide instant answers, such as checking if your grocery budget has been exceeded or providing a savings prediction.

-----

## 🛠️ Technologies Used

  - **Framework**: Streamlit
  - **Data Science & Manipulation**: Pandas, NumPy
  - **Data Visualization**: Plotly Express, Matplotlib, Seaborn
  - **AI & NLP**: OpenAI API
  - **Speech Recognition**: SpeechRecognition
  - **Core Language**: Python 3
  - **Utilities**: subprocess, calendar, json, os

-----

## 📁 Project Structure

A recommended structure for this project would be:

```bash
.
├── assets/
│   ├── dashboard.png       # Screenshot of the dashboard
│   └── chatbot.png         # Screenshot of the chatbot
├── main.py                 # Main Streamlit dashboard application
├── chatbot.py              # AI chatbot assistant application
├── myLogo.png              # Logo file used in the dashboard
├── animation_5.gif         # Animation file used in the dashboard
├── requirements.txt        # File with all project dependencies
└── README.md               # You are here!
```

-----

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/money-mind-pal.git
cd money-mind-pal
```

### 2\. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3\. Install Dependencies

Create a `requirements.txt` file with the following content:

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

Then, install all dependencies at once:

```bash
pip install -r requirements.txt
```

*Note: You may also need to install `PyAudio` for the speech recognition feature to work.*

### 4\. Add Your OpenAI API Key

> **⚠️ IMPORTANT SECURITY NOTE**
> The `chatbot.py` file contains a hardcoded API key. This is a significant security risk. For your safety, invalidate that key and use a secure method to store your new key.

It is highly recommended to use environment variables. **In `chatbot.py`, replace this:**

```python
api_key = "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"
openai.api_key = api_key
```

**With this:**

```python
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
```

You can then set the environment variable in your terminal before running the app.

-----

## 🚀 How to Use

**1. Running the Main Dashboard**
To start the main financial dashboard, run the following command in your terminal:

```bash
streamlit run main.py
```

This will open the application in your default web browser.

**2. Using the Chatbot**
The chatbot can be launched by clicking the **"Chatbot"** button in the dashboard's sidebar or by running it directly from your terminal:

```bash
streamlit run chatbot.py
```

-----

## 🧠 Sample Dataset & Prompts

The application fetches data from a public CSV file. For all features to work correctly, the data should contain at least these columns: `DATE`, `WITHDRAWAL AMT`, `DEPOSIT AMT`, `CATEGORY`.

**Example Prompts to Try with the Chatbot:**

  - "How much did I save last month?"
  - "Show me a graph of my deposits over time."
  - "What is the category-wise spending distribution?"
  - "Did I exceed my grocery budget?"
  - "What percentage of my income is spent on transportation?"
  - (Voice Command) "Give me a savings prediction for the next 6 months."

-----

## 📷 Screenshots

#### **Dashboard View**
![Dashboard Screenshot](./dashboard.jpg)

#### **AI Chatbot Interface**
![Chatbot Screenshot](./chatbot.jpg)

-----

## 🔮 Future Improvements

  - **Secure API Key Management**: Fully integrate environment variables or a `.env` file for storing the OpenAI API key.
  - **Dynamic Notifications**: Replace the hardcoded dashboard notifications with alerts generated dynamically from the user's data.
  - **Seamless App Integration**: Combine the two Streamlit apps into a single, multi-page application instead of using `subprocess`.
  - **Improved Chatbot Context**: Remove hardcoded chatbot responses and improve its ability to derive all insights directly from the provided financial data.
  - **User Authentication**: Implement a login system to allow multiple users to manage their own financial data securely.

-----

## 📌 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as you see fit.

-----

## 🙏 Acknowledgements

This project would not be possible without the incredible work from the following open-source communities and services:

  - [Streamlit](https://streamlit.io/)
  - [OpenAI API](https://platform.openai.com/)
  - [Plotly](https://plotly.com/python/)
  - [Pandas](https://pandas.pydata.org/)
  - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
  - [Seaborn & Matplotlib](https://seaborn.pydata.org/)
