# 🤖 Tiny AI Q&A Bot (Gemini Edition)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Status](https://img.shields.io/badge/status-completed-green)

---

## **Overview**

A simple **AI-powered chatbot** built using **Google Gemini API** and **Streamlit**. Users can ask questions and get instant AI-generated answers in a clean, interactive chat interface.

The goal of this project is to showcase **AI integration, UI design, and session management** in a simple yet functional chatbot app.

---

## **Features**

* Real-time AI Q&A responses
* Scrollable chat container with persistent session history
* Input box pinned at the bottom for natural chat layout
* Chat bubbles: **green for user**, **lavender for AI**
* Auto-scroll to the latest message
* HTML-safe AI output to prevent layout issues

---

## **Tech Stack**

| Component       | Technology                                          |
| --------------- | --------------------------------------------------- |
| Frontend/UI     | Streamlit                                           |
| AI Model        | Google Gemini API                                   |
| Python Packages | `google-generativeai`, `streamlit`, `python-dotenv` |

---

## **Setup & Installation**

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/tiny-ai-qa-bot.git
cd tiny-ai-qa-bot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set API Key** in `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

> ⚠️ Never commit your real API key to GitHub.

4. **Run the app**

```bash
streamlit run app.py
```

5. Open the app in your browser and start chatting!

---

## **Usage**

1. Type your question in the input box at the bottom.
2. Click **Ask** to get AI-generated answers.
3. Scroll through previous messages in the chat container.
4. Close the browser tab to end the session (chat history persists only during the session).

---

## **Development Notes**

* Used `.env` and `python-dotenv` to handle API keys securely.
* Managed chat history with **Streamlit `session_state`**.
* Fixed HTML rendering issues using `html.escape()`.
* Designed a **scrollable chat container** and pinned input box at the bottom.
* Tested various AI questions and verified reliable responses.

---
## Screenshots

**Chat Interface:**  
![Chat Opening](screenshots/chat_opening.png)

**User Question:**  
![User Question](screenshots/user_question.png)

**AI Response:**  
![AI Response](screenshots/ai_response.png)

## **Future Improvements**

* Add full **dark mode** support
* Press **Enter** to send messages
* Save chat history permanently in a database
* Deploy online on **Streamlit Cloud / Render / HuggingFace Spaces**
* Add **voice input** and multi-turn conversation context

---

## **Dependencies**

| Package             | Version |
| ------------------- | ------- |
| streamlit           | 1.28.0  |
| google-generativeai | 0.3.0   |
| python-dotenv       | 1.0.0   |

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---


