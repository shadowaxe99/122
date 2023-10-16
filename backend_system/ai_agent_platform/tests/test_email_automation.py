import unittest
from backend_system.ai_agent_platform.email_automation import EmailAutomation

class TestEmailAutomation(unittest.TestCase):

    def setUp(self):
        self.email_automation = EmailAutomation()

    def test_send_email(self):
        result = self.email_automation.send_email("test@brand.com", "Test Subject", "Test Message")
        self.assertTrue(result)

    def test_track_response(self):
        self.email_automation.send_email("test@brand.com", "Test Subject", "Test Message")
        response = self.email_automation.track_response("test@brand.com")
        self.assertIsNotNone(response)

    def test_email_count(self):
        initial_count = self.email_automation.email_count
        self.email_automation.send_email("test@brand.com", "Test Subject", "Test Message")
        self.assertEqual(self.email_automation.email_count, initial_count + 1)

    def test_response_count(self):
        initial_count = self.email_automation.response_count
        self.email_automation.send_email("test@brand.com", "Test Subject", "Test Message")
        self.email_automation.track_response("test@brand.com")
        self.assertEqual(self.email_automation.response_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()