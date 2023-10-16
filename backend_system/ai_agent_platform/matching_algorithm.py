```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from user_profile_management import UserProfile
from brand_database import BrandDatabase

class MatchingAlgorithm:
    def __init__(self):
        self.user_profiles = UserProfile()
        self.brand_database = BrandDatabase()

    def generate_feature_vectors(self, user_preferences, brand_attributes):
        user_vector = np.array([user_preferences[attr] for attr in brand_attributes])
        brand_vectors = np.array([brand[attr] for brand in self.brand_database.brands for attr in brand_attributes])
        return user_vector, brand_vectors

    def match_influencer_to_brand(self, influencer_id):
        influencer_preferences = self.user_profiles.get_preferences(influencer_id)
        brand_attributes = self.brand_database.get_attributes()

        user_vector, brand_vectors = self.generate_feature_vectors(influencer_preferences, brand_attributes)

        similarity_scores = cosine_similarity([user_vector], brand_vectors)
        top_brand_index = np.argmax(similarity_scores)
        top_brand_match = self.brand_database.brands[top_brand_index]

        return top_brand_match
```