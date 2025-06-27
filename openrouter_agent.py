import requests
import re

def get_response_from_openrouter(prompt):
    headers = {
        "Authorization": "Bearer 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",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json",
    }

    system_prompt = """You are a professional email assistant with 10+ years of experience in business communication.
    Your task is to generate professional, concise, and contextually appropriate email replies.
    Guidelines:
    - Write in a professional but friendly tone
    - Keep responses concise (2-4 sentences)
    - Address the sender appropriately
    - Provide clear, actionable responses
    - Do NOT include subject lines, signatures, or formatting
    - Focus only on the reply content
    - If the email is unclear, ask for clarification politely
    Generate ONLY the reply content, nothing else."""

    data = {
        "model": "google/gemma-3-27b-it:free",  # or "google/gemma-7b-it:free" or your available free Gemma model
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Generate a professional reply to this email: {prompt}"}
        ],
        "max_tokens": 300,
        "temperature": 0.3,
        "top_p": 0.9
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        res_json = response.json()

        if response.status_code != 200:
            return f"API Error: {res_json.get('error', {}).get('message', 'Unknown error')}"

        if "choices" not in res_json or not res_json["choices"]:
            return "Unable to generate response. Please try again."

        content = res_json["choices"][0]["message"]["content"]
        content = clean_response_content(content)
        return content

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Network error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def clean_response_content(content):
    if not content:
        return "Thank you for your email. I'll get back to you soon."
    content = re.sub(r'Subject:\s*.*?\n', '', content, flags=re.IGNORECASE)
    content = re.sub(r'Dear\s*\[.*?\]', 'Thank you', content)
    content = re.sub(r'\[.*?\]', '', content)
    content = re.sub(r'Best regards,?\s*\[.*?\]', '', content, flags=re.IGNORECASE)
    content = re.sub(r'Looking forward to.*?\.', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\n\s*\n', '\n', content)
    content = content.strip()
    if len(content) < 10 or content.count('[') > content.count(']'):
        return "Thank you for your email. I appreciate you reaching out and will respond in detail soon."
    return content