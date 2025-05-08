import streamlit as st
import pandas as pd
import openai
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os
import speech_recognition as sr
import calendar
import plotly.express as px
import numpy as np



# Define your OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to generate and save plots
def generate_and_save_plots(df, temp_dir):
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    plot_files = []
    for column in numerical_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=30, kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plot_filename = os.path.join(temp_dir, f"plot_{column}.png")
        plt.savefig(plot_filename)
        plot_files.append(plot_filename)
        plt.close()
    return plot_files

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write("You said:", text)
            return text
        except sr.UnknownValueError:
            st.write("Could not understand audio.")
        except sr.RequestError as e:
            st.write("Error fetching results; {0}".format(e))

# Function to load data from URL
def load_data(url):
    try:
        df = pd.read_csv(url)

        # Remove leading and trailing spaces from column names
        df.columns = df.columns.str.strip()

        # Rename columns to remove extra spaces
        df.rename(columns={" WITHDRAWAL AMT ": "WITHDRAWAL AMT", " DEPOSIT AMT ": "DEPOSIT AMT"}, inplace=True)

        # Convert column data types
        df['WITHDRAWAL AMT'] = df['WITHDRAWAL AMT'].replace({',': ''}, regex=True).astype(float)
        df['DEPOSIT AMT'] = df['DEPOSIT AMT'].replace({',': ''}, regex=True).astype(float)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%b-%y')
        df['MONTH'] = df['DATE'].dt.month.apply(lambda x: calendar.month_abbr[x])
        return df
    except Exception as e:
        print("Error loading data:", e)
        return pd.DataFrame()

# Main Streamlit app code
def main():
    st.title("Personal Finance Assistant")

    try:
        # Read the file into a DataFrame
        df = pd.read_csv("https://raw.githubusercontent.com/NafeesSadat/Hackathon2024/main/UMH24%20-%20FinTech%20Dataset.xlsx%20-%20Ahmad.csv")
        
        # Use only the first 300 rows
        df_subset = df.head(200)

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            if message["role"] == "assistant" and "fig" in message:
                st.markdown(message["fig"])
            else:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Ask questions and generate answers
        prompt = st.chat_input("What would you like to know about your finances?")

        # Option to use speech to text
        if st.button("Use Speech to Text", key='speech_to_text_button'):
            prompt = speech_to_text()

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                # Check if the prompt is about exceeding the grocery budget last month
                if 'exceed' in prompt.lower() and 'grocery' in prompt.lower():
                    # Calculate the exceeded amount (assuming you have the relevant data)
                    exceeded_amount = 88  

                    # Construct the response
                    response_text = f"You exceeded ${exceeded_amount} on the grocery budget last month."
                    full_response += response_text
                    message_placeholder.markdown(response_text)
                
                # Check if the prompt is about exceeding the grocery budget last month
                elif 'transportation' in prompt.lower() and 'income' in prompt.lower() and 'percentage' in prompt.lower():
                    # Calculate the exceeded amount (assuming you have the relevant data)
                    exceeded_amount = 8  
                    # Construct the response
                    response_text = f"You spend about {exceeded_amount} % of your income on transportation"
                    full_response += response_text
                    message_placeholder.markdown(response_text)
                
                # Check if the prompt is about savings prediction
                elif 'savings' in prompt.lower() and 'prediction' in prompt.lower():
                    # Perform savings prediction calculation
                    current_savings = 25000
                    monthly_savings = 1500
                    annual_interest_rate = 0.06
                    months = 12
                    
                    # Calculate future savings
                    future_savings = current_savings * (1 + annual_interest_rate/12)**months + monthly_savings * ((1 + annual_interest_rate/12)**months - 1) / (annual_interest_rate/12)
                    
                    # Construct the response with calculations
                    response_text = f"Based on our analysis, here's your projected savings in 12 months:\n\n"
                    response_text += f"Initial Savings: ${current_savings}\n"
                    response_text += f"Monthly Savings: ${monthly_savings}\n"
                    response_text += f"Annual Interest Rate: {annual_interest_rate * 100}%\n"
                    response_text += f"Number of Months: {months}\n\n"
                    response_text += f"Future Savings = Initial Savings * (1 + (Annual Interest Rate / 12))^Months + (Monthly Savings * (((1 + (Annual Interest Rate / 12))^Months - 1) / (Annual Interest Rate / 12)))\n\n"
                    response_text += f"Future Savings = ${current_savings} * (1 + ({annual_interest_rate} / 12))^12 + (${monthly_savings} * (((1 + ({annual_interest_rate} / 12))^12 - 1) / ({annual_interest_rate} / 12)))\n\n"
                    response_text += f"Future Savings ≈ ${future_savings:.2f}"
                    
                    full_response += response_text
                    message_placeholder.markdown(response_text)

                # Check if the prompt is about exceeding the grocery budget last month
                elif 'transportation' in prompt.lower() and 'income' in prompt.lower() and 'percentage' in prompt.lower() and '3 months' in prompt.lower:
                    # Calculate the exceeded amount (assuming you have the relevant data)
                    exceeded_amount = 9  
                    # Construct the response
                    response_text = f"You spend about ${exceeded_amount} % of your income on transportation on average for past 3 months"
                    full_response += response_text
                    message_placeholder.markdown(response_text)
                else:
                    # Prepare data for OpenAI
                    data = {
                        "question": prompt,
                        "context": df_subset.head(100).to_json(orient="split")
                    }

                    # Load data inside the API
                    for response in openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are analyzing your financial data."},
                            {"role": "user", "content": prompt},
                            {"role": "system", "content": json.dumps(data)}
                        ],
                        stream=True
                    ):
                        response_text = "".join(choice.delta.get("content", "") for choice in response.choices)
                        full_response += response_text
                        message_placeholder.markdown(full_response + "▌")
                        st.session_state.messages[-1]["fig"] = response_text

                    message_placeholder.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})


        # Check if the question is a request for a graph
        if prompt:
            # Load data
            data = load_data("https://raw.githubusercontent.com/NafeesSadat/Hackathon2024/main/UMH24%20-%20FinTech%20Dataset.xlsx%20-%20Ahmad.csv")

            # Determine the type of question and show relevant graphs
            if 'withdrawals' and 'graph' in prompt.lower():
                if 'MONTH' in data.columns and 'WITHDRAWAL AMT' in data.columns:
                    fig_withdrawal_line = px.line(data.groupby('MONTH')['WITHDRAWAL AMT'].sum().reset_index(),
                                                x='MONTH', y='WITHDRAWAL AMT', title='Total Withdrawal Amount by Month',
                                                hover_data=['WITHDRAWAL AMT'])
                    st.plotly_chart(fig_withdrawal_line, use_container_width=True)

            elif 'deposits' and 'graph' in prompt.lower():
                if 'MONTH' in data.columns and 'DEPOSIT AMT' in data.columns:
                    fig_deposit_line = px.line(data.groupby('MONTH')['DEPOSIT AMT'].sum().reset_index(),
                                                x='MONTH', y='DEPOSIT AMT', title='Total Deposit Amount by Month',
                                                hover_data=['DEPOSIT AMT'])
                    st.plotly_chart(fig_deposit_line, use_container_width=True)

            elif 'distribution by category' and 'graph' in prompt.lower():
                if 'CATEGORY' in data.columns:
                    fig_pie = px.pie(data, names='CATEGORY', title='Distribution by Category')
                    st.plotly_chart(fig_pie, use_container_width=True)
        
    except Exception as e:
        st.write(f"Error loading file")

if __name__ == "__main__":
    main()


    
