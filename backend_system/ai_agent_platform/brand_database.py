```python
import pymongo
from pymongo import MongoClient
from security import encrypt_data, decrypt_data

class BrandDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['ai_agent_platform']
        self.collection = self.db['brands']

    def add_brand(self, brand_data):
        encrypted_data = encrypt_data(brand_data)
        self.collection.insert_one(encrypted_data)

    def get_brand(self, brand_id):
        brand_data = self.collection.find_one({'_id': brand_id})
        if brand_data:
            return decrypt_data(brand_data)
        else:
            return None

    def update_brand(self, brand_id, brand_data):
        encrypted_data = encrypt_data(brand_data)
        self.collection.update_one({'_id': brand_id}, {"$set": encrypted_data})

    def delete_brand(self, brand_id):
        self.collection.delete_one({'_id': brand_id})

    def get_all_brands(self):
        brands = self.collection.find()
        return [decrypt_data(brand) for brand in brands]

if __name__ == "__main__":
    db = BrandDatabase()
    db.add_brand({"name": "Brand1", "category": "Fashion", "budget": 10000})
    print(db.get_all_brands())
```