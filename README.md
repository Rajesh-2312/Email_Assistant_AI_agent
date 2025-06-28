
# AI Email Assistant

An intelligent email auto-responder powered by OpenRouter's AI models and Gmail API. This application automatically generates professional email replies using AI and provides a user-friendly Streamlit interface for managing email responses.

## Features

- **AI-Powered Email Replies**: Uses OpenRouter's Google Gemma models to generate contextual and professional email responses
- **Gmail Integration**: Seamlessly connects with Gmail API to fetch and send emails
- **Streamlit Web Interface**: Modern, intuitive web interface for managing email interactions
- **Real-time Email Processing**: Fetch unread emails and generate AI responses instantly
- **Editable AI Responses**: Review and edit AI-generated replies before sending
- **Professional Communication**: Maintains business-appropriate tone and formatting

##  Prerequisites

- Python 3.7 or higher
- Gmail account with API access
- OpenRouter API key (free tier available)
- Google Cloud Console project with Gmail API enabled

##  Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/openrouter-email-agent.git
   cd openrouter-email-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud Console**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Download `credentials.json` and place it in the project root

4. **Configure OpenRouter API**
   - Sign up at [OpenRouter](https://openrouter.ai/) (free tier available)
   - Get your API key
   - Replace the API key in `openrouter_agent.py` (line 5)

## Configuration

### Gmail API Setup
1. Download `credentials.json` from Google Cloud Console
2. Place it in the project root directory
3. The application will automatically generate `token.json` on first run

### OpenRouter API Setup
1. Get your API key from [OpenRouter Dashboard](https://openrouter.ai/keys)
2. Replace the API key in `openrouter_agent.py`:
   ```python
   "Authorization": "Bearer YOUR_API_KEY_HERE"
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`
   - The application will open automatically

3. **Using the Email Assistant**
   - Click "Fetch Unread Emails" to retrieve new emails
   - Review each email and its AI-generated reply
   - Edit the reply if needed
   - Click "Send Reply" to send the response

##  Security Notes

- **Never commit sensitive files**: `credentials.json` and `token.json` are excluded from version control
- **API Keys**: Keep your OpenRouter API key secure and don't share it publicly
- **Gmail Permissions**: The app only requests Gmail modify permissions for sending/receiving emails

##  AI Models Used

- **Primary Model**: Google Gemma 3 27B (free tier)
- **Alternative**: Google Gemma 7B (free tier)
- **Customization**: Easy to switch models by modifying `openrouter_agent.py`
- **Customization** : Google AI Studio API key `aistudio.google.com`

##  Features in Detail

### Email Processing
- Fetches unread emails from Gmail
- Extracts sender, subject, and body content
- Handles email threading and formatting

### AI Response Generation
- Professional tone and business-appropriate language
- Context-aware responses based on email content
- Concise and actionable replies
- Automatic content cleaning and formatting

### User Interface
- Clean, modern Streamlit interface
- Real-time email fetching
- Editable AI responses
- Success/error notifications
- Email management tools

##  Troubleshooting

### Common Issues

1. **Gmail Authentication Error**
   - Ensure `credentials.json` is in the project root
   - Delete `token.json` and re-authenticate
   - Check Gmail API is enabled in Google Cloud Console

2. **OpenRouter API Error**
   - Verify API key is correct in `openrouter_agent.py`
   - Check OpenRouter account status and usage limits
   - Ensure internet connection is stable

3. **Streamlit Connection Issues**
   - Check if port 8501 is available
   - Try running with `streamlit run streamlit_app.py --server.port 8502`

##  License

This project is open source and available under the [MIT License](LICENSE).

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

##  Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the [OpenRouter Documentation](https://openrouter.ai/docs)
3. Check [Gmail API Documentation](https://developers.google.com/gmail/api)

##  Updates

- **v1.0**: Initial release with basic email auto-response functionality
- **v1.1**: Added Streamlit interface and improved AI response quality
- **v1.2**: Enhanced security and error handling

---

**Note**: This application uses free tier services from OpenRouter and Google Cloud. Be mindful of API usage limits and costs when scaling up.
