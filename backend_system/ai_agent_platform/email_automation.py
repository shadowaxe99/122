```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_profile_management import get_user_data
from response_tracking import record_response

def send_email(user_id, brand_id, partnership_idea):
    user_data = get_user_data(user_id)
    brand_data = get_brand_data(brand_id)

    # Create message
    msg = MIMEMultipart()
    msg['From'] = 'noreply@aiagentplatform.com'
    msg['To'] = brand_data['email']
    msg['Subject'] = f"Partnership Proposal from {user_data['name']}"

    # Create the body of the message
    body = f"Dear {brand_data['name']},\n\n"
    body += f"We are excited to propose a partnership between your brand and {user_data['name']}."
    body += f"\n\nPartnership Idea:\n{partnership_idea}\n\n"
    body += "We look forward to hearing from you.\n\nBest,\nAI Agent Platform Team"

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Send the message via the server set up earlier.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

    # Record the email sent
    record_response(user_id, brand_id, 'email_sent')

def get_brand_data(brand_id):
    # This function will be implemented in brand_database.py
    pass
```