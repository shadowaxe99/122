import unittest
from backend_system.ai_agent_platform.matching_algorithm import MatchingAlgorithm
from backend_system.ai_agent_platform.user_profile_management import UserProfileManagement
from backend_system.ai_agent_platform.brand_database import BrandDatabase

class TestMatchingAlgorithm(unittest.TestCase):

    def setUp(self):
        self.user_profile_management = UserProfileManagement()
        self.brand_database = BrandDatabase()
        self.matching_algorithm = MatchingAlgorithm(self.user_profile_management, self.brand_database)

    def test_match_influencer_to_brand(self):
        # Add a test influencer and brand
        influencer_id = self.user_profile_management.add_influencer("Test Influencer", "Fashion")
        brand_id = self.brand_database.add_brand("Test Brand", "Fashion")

        # Run the matching algorithm
        matches = self.matching_algorithm.match_influencer_to_brand(influencer_id)

        # Check that the brand is in the matches
        self.assertIn(brand_id, matches)

    def test_no_match_influencer_to_brand(self):
        # Add a test influencer and brand
        influencer_id = self.user_profile_management.add_influencer("Test Influencer", "Fashion")
        brand_id = self.brand_database.add_brand("Test Brand", "Tech")

        # Run the matching algorithm
        matches = self.matching_algorithm.match_influencer_to_brand(influencer_id)

        # Check that the brand is not in the matches
        self.assertNotIn(brand_id, matches)

    def test_match_brand_to_influencer(self):
        # Add a test influencer and brand
        influencer_id = self.user_profile_management.add_influencer("Test Influencer", "Fashion")
        brand_id = self.brand_database.add_brand("Test Brand", "Fashion")

        # Run the matching algorithm
        matches = self.matching_algorithm.match_brand_to_influencer(brand_id)

        # Check that the influencer is in the matches
        self.assertIn(influencer_id, matches)

    def test_no_match_brand_to_influencer(self):
        # Add a test influencer and brand
        influencer_id = self.user_profile_management.add_influencer("Test Influencer", "Fashion")
        brand_id = self.brand_database.add_brand("Test Brand", "Tech")

        # Run the matching algorithm
        matches = self.matching_algorithm.match_brand_to_influencer(brand_id)

        # Check that the influencer is not in the matches
        self.assertNotIn(influencer_id, matches)

if __name__ == '__main__':
    unittest.main()