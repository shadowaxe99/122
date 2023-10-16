import unittest
from backend_system.ai_agent_platform import security

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "username": "test_influencer",
            "password": "test_password",
            "preferences": ["brand1", "brand2"]
        }
        self.brand_data = {
            "brand_name": "test_brand",
            "brand_info": "test_info"
        }

    def test_encrypt_decrypt(self):
        encrypted_data = security.encrypt_data(self.user_data)
        decrypted_data = security.decrypt_data(encrypted_data)
        self.assertEqual(self.user_data, decrypted_data, "Decrypted data should match original data")

    def test_firewall(self):
        is_blocked = security.firewall(self.user_data)
        self.assertFalse(is_blocked, "Valid user data should not be blocked by firewall")

    def test_security_audit(self):
        vulnerabilities = security.security_audit()
        self.assertEqual(vulnerabilities, [], "Security audit should not find any vulnerabilities")

    def test_incident_response(self):
        incident = {"type": "data breach", "data": self.user_data}
        response = security.incident_response(incident)
        self.assertTrue(response, "Incident response should be successful")

    def test_gdpr_compliance(self):
        is_compliant = security.check_gdpr_compliance(self.user_data)
        self.assertTrue(is_compliant, "User data should be GDPR compliant")

    def test_data_deletion(self):
        is_deleted = security.delete_user_data(self.user_data["username"])
        self.assertTrue(is_deleted, "User data should be deleted successfully")

if __name__ == "__main__":
    unittest.main()