import streamlit as st
from email_listener import fetch_latest_email
from email_sender import send_email
from gemini_agent import get_response_from_gemini
import uuid


st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("AI Auto Email Assistant")

if "emails" not in st.session_state:
    st.session_state.emails = []
if "replies" not in st.session_state:
    st.session_state.replies = {}
if "sent" not in st.session_state:
    st.session_state.sent = {}

if st.button("Fetch Unread Emails"):
    emails = fetch_latest_email()
    st.session_state.emails = emails
    st.session_state.replies = {}
    st.session_state.sent = {}

if not st.session_state.emails:
    st.info("No unread emails found. Click 'Fetch Unread Emails' to check again.")
else:
    for idx, email_data in enumerate(st.session_state.emails):
        email_key = f"email_{idx}"
        reply_key = f"reply_{idx}"
        send_key = f"send_{idx}"

        with st.expander(f"From: {email_data['sender']} | Subject: {email_data['subject']}", expanded=True):
            st.write("**Email Body:**")
            st.write(email_data['body'])

            # Generate AI reply if not already done
            if reply_key not in st.session_state.replies:
                ai_reply = get_response_from_gemini(email_data['body'])
                st.session_state.replies[reply_key] = ai_reply

            # Editable text area for the reply
            st.session_state.replies[reply_key] = st.text_area(
                "AI Generated Reply (edit before sending):",
                value=st.session_state.replies[reply_key],
                key=reply_key,
                height=150
            )

            # Send button
            if not st.session_state.sent.get(send_key, False):
                if st.button("Send Reply", key=send_key):
                    try:
                        send_email(email_data['sender'], f"Re: {email_data['subject']}", st.session_state.replies[reply_key])
                        st.session_state.sent[send_key] = True
                        st.success(f"Reply sent to {email_data['sender']}")
                    except Exception as e:
                        st.error(f"Failed to send email: {str(e)}")
            else:
                st.success("Reply sent!")



if 'emails' not in st.session_state:
    st.session_state['emails'] = fetch_latest_email()

st.write("Fetched Emails:")

# Display each email with its own "Clear" button
remove_idx = None
for idx, email in enumerate(st.session_state['emails']):
    with st.expander(f"From: {email['sender_name']} | Subject: {email['subject']}"):
        st.write(f"Body: {email['body']}")
        # Unique key for each button
        if st.button("Clear", key=f"clear_{idx}"):
            remove_idx = idx

# Remove the email after the loop to avoid modifying the list during iteration
if remove_idx is not None:
    st.session_state['emails'].pop(remove_idx)
    st.rerun()