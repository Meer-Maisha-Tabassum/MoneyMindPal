````markdown
💰 Money Mind Pal — Personal Finance Dashboard with AI Chat Assistant

Money Mind Pal is an interactive **Streamlit-based financial dashboard** enhanced with an **AI-powered chatbot assistant**. It helps users visualize their spending and saving habits, ask financial questions via text or voice, and receive intelligent, data-driven insights — all from their transaction history.

---

## 📊 Features

### 🔹 Streamlit Dashboard (`main.py`)
- 📈 Visualizes total deposits and withdrawals by month using Plotly charts.
- 🧮 Cleans and processes CSV financial transaction data.
- 🖼️ Stylish sidebar branding with logo and title.
- 🔔 Custom notification dropdown with user tips.
- 🧠 Simple and accessible UI to trigger the financial dashboard.

### 🔹 AI Chatbot Assistant (`chatbot.py`)
- 💬 Interactive financial Q&A via chat interface.
- 🎙️ Voice recognition support (Speech-to-Text using `speech_recognition`).
- 🤖 Answers finance-related prompts using OpenAI's `gpt-3.5-turbo` model.
- 📊 Automatically renders context-based charts for:
  - Withdrawals by month
  - Deposits by month
  - Spending distribution by category
- 🔐 Includes hardcoded OpenAI API key (for demo purposes; replace for security).
- 🧠 Some hardcoded logic for quick queries:
  - Grocery budget exceeded
  - Transportation cost as % of income
  - Savings prediction (with formula shown)

---

## 📁 Project Structure

```bash
.
├── main.py         # Streamlit dashboard UI
├── chatbot.py      # AI chatbot with OpenAI & voice input
├── requirements.txt  # (recommended) install dependencies
└── README.md       # Project documentation
````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

We recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

Or manually install the core packages:

```bash
pip install streamlit pandas openai seaborn matplotlib plotly speechrecognition
```

### 3. Run the Streamlit App

To launch the AI chatbot:

```bash
streamlit run chatbot.py
```

To launch the dashboard view:

```bash
streamlit run main.py
```

---

## 🧠 Sample Dataset

Both files fetch data from this public CSV URL:

```
https://raw.githubusercontent.com/NafeesSadat/Hackathon2024/main/UMH24%20-%20FinTech%20Dataset.xlsx%20-%20Ahmad.csv
```

The dataset should contain at least the following columns:

* `DATE`
* `WITHDRAWAL AMT`
* `DEPOSIT AMT`
* `CATEGORY`

---

## 🔐 Security Note

> ⚠️ Your OpenAI API key is currently **hardcoded** in `chatbot.py`:

```python
api_key = "sk-..."
```

For security:

* Use `os.environ["OPENAI_API_KEY"]` or
* Store the key in a `.env` file and load using `python-dotenv`.

---

## 🚀 Example Prompts to Try

* **"Did I exceed my grocery budget last month?"**
* **"How much do I spend on transportation as a percentage of income?"**
* **"Give me a savings prediction for 12 months."**
* **"Show me the graph for deposits."**
* **"What is the category-wise spending distribution?"**

You can also click the **"Use Speech to Text"** button and speak your query!

---

## 📷 Screenshots

| Dashboard                            | AI Chatbot                       |
| ------------------------------------ | -------------------------------- |
| ![dashboard](./assets/dashboard.png) | ![chatbot](./assets/chatbot.png) |

> **(Replace with your actual screenshots in an `assets/` folder)**

---

## 📌 License

MIT License. Free to use and adapt.

---

## 👨‍💻 Author

Made with ❤️ for **Hackathon 2024**
By \Meer Maisha Tabassum

---

## 🙏 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [OpenAI API](https://platform.openai.com/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [Plotly](https://plotly.com/python/)
* [Pandas](https://pandas.pydata.org/)
* [Seaborn + Matplotlib](https://seaborn.pydata.org/)

```
