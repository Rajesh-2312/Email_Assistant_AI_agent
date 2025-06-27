# OpenRouter AI Email Agent (No .env)

A simple email auto-responder using Gmail API and OpenRouter's free Google Flash model.

## Setup

1. Download `credentials.json` from Google Cloud and place in project root.
2. Replace OpenRouter key directly in `openrouter_agent.py`.
3. Run:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```