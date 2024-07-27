# Chatbot with Gemini Pro and Streamlit

This project is a chatbot application that uses the Gemini Pro API to interact with users in a natural and coherent manner. The chatbot is capable of understanding and responding to various user queries through a simple and user-friendly frontend interface built with Streamlit.

## Overview

The chatbot leverages the power of a large language model (LLM) via the Gemini Pro API to provide accurate and meaningful responses to user inputs. The frontend interface, developed using Streamlit, allows users to interact with the chatbot seamlessly.

## Features

- Understands and responds to user queries accurately.
- Simple and intuitive user interface built with Streamlit.
- Utilizes the Gemini Pro API for powerful language model capabilities.

## Demo Video

Watch the [demo video](https://github.com/Disha4346/chatbot-project/blob/main/video-demo/pdf%20analyzer.mp4) to see the chatbot in action.


## Installation

Follow these steps to set up and run the chatbot:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Disha4346/chatbot-project.git
    cd chatbot-project
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the Gemini Pro API key:**
   - Create a `.env` file in the project root directory.
   - Add your Gemini Pro API key to the `.env` file:
     ```
     GEMINI_PRO_API_KEY=your_api_key_here
     ```

4. **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Usage

- Open the browser and navigate to the URL displayed in the terminal after running the above command.
- Interact with the chatbot by typing your queries in the input box and receiving responses in real-time.

## Project Structure

```
chatbot-project/
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables file
├── README.md               # Project documentation
```



This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Gemini Pro API](https://example.com)
- [Streamlit](https://streamlit.io)

