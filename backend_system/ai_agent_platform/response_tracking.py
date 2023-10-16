```python
import json
from email_automation import send_email

class ResponseTracker:
    def __init__(self):
        self.responses = {}

    def track_response(self, email_id, response):
        if email_id not in self.responses:
            self.responses[email_id] = []
        self.responses[email_id].append(response)

    def get_responses(self, email_id):
        return self.responses.get(email_id, [])

    def save_responses(self):
        with open('responses.json', 'w') as f:
            json.dump(self.responses, f)

    def load_responses(self):
        try:
            with open('responses.json', 'r') as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            self.responses = {}

if __name__ == "__main__":
    tracker = ResponseTracker()
    tracker.load_responses()

    # Simulate tracking a response
    email_id = send_email("brand@example.com", "Influencer Partnership Proposal", "Dear Brand, ...")
    tracker.track_response(email_id, "Interested, tell me more.")

    tracker.save_responses()
```