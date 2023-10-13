import unittest
from backend_system.ai_agent_platform.pitch_deck_generator import PitchDeckGenerator

class TestPitchDeckGenerator(unittest.TestCase):

    def setUp(self):
        self.pitch_deck_generator = PitchDeckGenerator()

    def test_generate_pitch_deck(self):
        influencer_profile = {
            'name': 'John Doe',
            'preferences': ['Fashion', 'Travel'],
            'followers': 10000
        }

        brand_profile = {
            'name': 'Brand X',
            'industry': 'Fashion',
            'budget': 5000
        }

        partnership_idea = 'Brand X and John Doe collaborate on a travel vlog featuring Brand X products.'

        pitch_deck = self.pitch_deck_generator.generate_pitch_deck(influencer_profile, brand_profile, partnership_idea)

        self.assertIsNotNone(pitch_deck)
        self.assertIn('John Doe', pitch_deck)
        self.assertIn('Brand X', pitch_deck)
        self.assertIn(partnership_idea, pitch_deck)

    def test_generate_pitch_deck_no_idea(self):
        influencer_profile = {
            'name': 'John Doe',
            'preferences': ['Fashion', 'Travel'],
            'followers': 10000
        }

        brand_profile = {
            'name': 'Brand X',
            'industry': 'Fashion',
            'budget': 5000
        }

        with self.assertRaises(ValueError):
            self.pitch_deck_generator.generate_pitch_deck(influencer_profile, brand_profile, None)

if __name__ == '__main__':
    unittest.main()