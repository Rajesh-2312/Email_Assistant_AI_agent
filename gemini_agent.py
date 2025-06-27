import os
import requests

os.environ["GOOGLE_API_KEY"] = "AIzaSyA_DnDP7LGFpEcTOtZf2bC_4uWUf_yJv2Y"
API_KEY = os.environ["GOOGLE_API_KEY"]

def get_response_from_gemini(prompt):
    system_prompt = """You are a professional email assistant with 10+ years of experience in business communication.\nYour task is to generate professional, concise, and contextually appropriate email replies.\nGuidelines:\n- Write in a professional but friendly tone\n- Keep responses concise (2-4 sentences)\n- Address the sender appropriately\n- Provide clear, actionable responses\n- Do NOT include subject lines, signatures, or formatting\n- Focus only on the reply content\n- If the email is unclear, ask for clarification politely\nGenerate ONLY the reply content, nothing else."""
    full_prompt = f"{system_prompt}\n\nEmail:\n{prompt}"
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}
    data = {
        "contents": [{"parts": [{"text": full_prompt}]}]
    }
    resp = requests.post(url, headers=headers, params=params, json=data)
    resp.raise_for_status()
    result = resp.json()
    return result["candidates"][0]["content"]["parts"][0]["text"].strip()