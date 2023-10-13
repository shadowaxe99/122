```python
import json
from matching_algorithm import match_influencer_brand
from partnership_idea_generator import generate_partnership_idea

class PitchDeckGenerator:
    def __init__(self):
        self.pitch_deck = {}

    def create_pitch_deck(self, influencer, brand):
        match_score = match_influencer_brand(influencer, brand)
        partnership_idea = generate_partnership_idea(influencer, brand)

        self.pitch_deck['influencer'] = influencer
        self.pitch_deck['brand'] = brand
        self.pitch_deck['match_score'] = match_score
        self.pitch_deck['partnership_idea'] = partnership_idea

        return self.pitch_deck

    def save_pitch_deck(self, pitch_deck):
        with open('pitch_deck.json', 'w') as json_file:
            json.dump(pitch_deck, json_file)

    def load_pitch_deck(self):
        with open('pitch_deck.json', 'r') as json_file:
            self.pitch_deck = json.load(json_file)
            return self.pitch_deck

if __name__ == "__main__":
    pitch_deck_generator = PitchDeckGenerator()
    pitch_deck = pitch_deck_generator.create_pitch_deck('influencer_1', 'brand_1')
    pitch_deck_generator.save_pitch_deck(pitch_deck)
    loaded_pitch_deck = pitch_deck_generator.load_pitch_deck()
    print(loaded_pitch_deck)
```