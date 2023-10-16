import unittest
from backend_system.ai_agent_platform.response_tracking import ResponseTracker

class TestResponseTracking(unittest.TestCase):

    def setUp(self):
        self.response_tracker = ResponseTracker()

    def test_record_response(self):
        response = {
            'email_id': '123',
            'brand_id': '456',
            'response': 'Interested'
        }
        self.response_tracker.record_response(response)
        self.assertIn(response, self.response_tracker.responses)

    def test_get_response_by_email_id(self):
        response = {
            'email_id': '123',
            'brand_id': '456',
            'response': 'Interested'
        }
        self.response_tracker.record_response(response)
        retrieved_response = self.response_tracker.get_response_by_email_id('123')
        self.assertEqual(response, retrieved_response)

    def test_get_response_by_brand_id(self):
        response = {
            'email_id': '123',
            'brand_id': '456',
            'response': 'Interested'
        }
        self.response_tracker.record_response(response)
        retrieved_response = self.response_tracker.get_response_by_brand_id('456')
        self.assertEqual(response, retrieved_response)

    def test_get_all_responses(self):
        response1 = {
            'email_id': '123',
            'brand_id': '456',
            'response': 'Interested'
        }
        response2 = {
            'email_id': '789',
            'brand_id': '012',
            'response': 'Not Interested'
        }
        self.response_tracker.record_response(response1)
        self.response_tracker.record_response(response2)
        all_responses = self.response_tracker.get_all_responses()
        self.assertIn(response1, all_responses)
        self.assertIn(response2, all_responses)

if __name__ == '__main__':
    unittest.main()