import unittest
from backend_system.ai_agent_platform.user_profile_management import UserProfileManagement

class TestUserProfileManagement(unittest.TestCase):

    def setUp(self):
        self.user_profile_management = UserProfileManagement()

    def test_store_influencer_profile(self):
        profile_data = {
            'name': 'Influencer A',
            'preferences': ['Brand X', 'Brand Y']
        }
        result = self.user_profile_management.store_influencer_profile(profile_data)
        self.assertEqual(result, True)

    def test_capture_influencer_preferences(self):
        preferences = ['Brand X', 'Brand Y']
        result = self.user_profile_management.capture_influencer_preferences(preferences)
        self.assertEqual(result, True)

    def test_get_influencer_profile(self):
        profile_data = {
            'name': 'Influencer A',
            'preferences': ['Brand X', 'Brand Y']
        }
        self.user_profile_management.store_influencer_profile(profile_data)
        result = self.user_profile_management.get_influencer_profile('Influencer A')
        self.assertEqual(result, profile_data)

    def test_update_influencer_profile(self):
        profile_data = {
            'name': 'Influencer A',
            'preferences': ['Brand X', 'Brand Y']
        }
        self.user_profile_management.store_influencer_profile(profile_data)
        updated_profile_data = {
            'name': 'Influencer A',
            'preferences': ['Brand Z']
        }
        result = self.user_profile_management.update_influencer_profile(updated_profile_data)
        self.assertEqual(result, True)

    def test_delete_influencer_profile(self):
        profile_data = {
            'name': 'Influencer A',
            'preferences': ['Brand X', 'Brand Y']
        }
        self.user_profile_management.store_influencer_profile(profile_data)
        result = self.user_profile_management.delete_influencer_profile('Influencer A')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()