# 📝 Tiny AI Q&A Bot – Development Journal

## **Day 1: Project Setup**

1. **Installed Python 3.10+** on Windows.
2. Created project folder: `tiny-ai-qa-bot_Ai project`.
3. Installed required packages:

   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```
4. Initialized GitHub repository and added `README.md` and `.gitignore`.
5. Attempted to create a CLI bot with **OpenAI API**:

   * ⚠️ Error: `Completion is no longer supported in openai>=1.0.0`
   * Research: OpenAI changed API → decided to use **Google Gemini API**.

---

## **Day 1: CLI Bot Prototype**

1. Created `cli_app.py` with Gemini API integration.
2. Tested Gemini API key:

   * ⚠️ Error: `GEMINI_API_KEY not found`
   * Tried directly in code → worked but not secure.
   * Fixed by creating `.env` file and loading key via `python-dotenv`.
3. Run CLI bot → AI responded correctly.

---

## **Day 2: Streamlit App**

1. Created `app.py` for web UI using Streamlit.
2. Added:

   * Text input
   * Ask button
   * Scrollable chat area
   * Display of AI responses
3. Tested API calls:

   * ⚠️ Error: `404 model gemini-1.5-flash not found`
   * Fixed by checking Gemini API documentation → used correct available model.
4. Chat history implementation:

   * Used `st.session_state.history`
   * ⚠️ Error: `st.session_state.input_box cannot be modified`
   * Resolved by correctly initializing `st.session_state.user_input`.

---

## **Day 2: UI Improvements**

1. Added **chat bubbles**:

   * Green for user
   * Lavender for AI
2. Pinned input box at bottom and scrollable chat history at top.
3. Auto-scroll to latest message.
4. Escaped HTML from AI to prevent layout breakage.
5. Tested multiple questions → all responses displayed correctly.

---

## **Day 2: Polishing & Submission Prep**

1. Created `.env.example` to safely store API key placeholder.
2. Added **screenshots** of app to `screenshots/` folder.
3. Finalized `requirements.txt` with:

   ```txt
   streamlit==1.28.0
   google-generativeai==0.3.0
   python-dotenv==1.0.0
   ```
4. Final testing:

   * CLI works
   * Streamlit app works
   * Chat history persists within session
5. Prepared **README.md** with overview, features, setup, usage, and screenshots.

---

## **Challenges & Learning**

* Gemini API key errors → solved with `.env` and `python-dotenv`.
* HTML breaking UI → solved using `html.escape()`.
* Streamlit session state errors → learned proper state management.
* Model version mismatch → checked Gemini documentation.

---

## **Future Improvements**

* Dark mode support
* Press **Enter** to send messages
* Save chat history permanently
* Deploy online (Streamlit Cloud, Render, HuggingFace Spaces)
* Add voice input and multi-turn context

---


