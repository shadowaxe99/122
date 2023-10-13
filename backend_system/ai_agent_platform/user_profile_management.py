```python
import json
from security import encrypt_data, decrypt_data

class UserProfile:
    def __init__(self, user_id, name, email, preferences):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.preferences = preferences

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

class UserProfileManager:
    def __init__(self):
        self.user_profiles = {}

    def add_user_profile(self, user_profile):
        encrypted_data = encrypt_data(user_profile.to_json())
        self.user_profiles[user_profile.user_id] = encrypted_data

    def get_user_profile(self, user_id):
        encrypted_data = self.user_profiles.get(user_id)
        if encrypted_data:
            decrypted_data = decrypt_data(encrypted_data)
            return UserProfile.from_json(decrypted_data)
        return None

    def update_user_profile(self, user_id, name=None, email=None, preferences=None):
        user_profile = self.get_user_profile(user_id)
        if user_profile:
            if name:
                user_profile.name = name
            if email:
                user_profile.email = email
            if preferences:
                user_profile.preferences = preferences
            self.add_user_profile(user_profile)

    def delete_user_profile(self, user_id):
        if user_id in self.user_profiles:
            del self.user_profiles[user_id]
```
