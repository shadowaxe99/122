import unittest
from backend_system.ai_agent_platform.analytics_dashboard import AnalyticsDashboard

class TestAnalyticsDashboard(unittest.TestCase):

    def setUp(self):
        self.analytics_dashboard = AnalyticsDashboard()

    def test_user_count(self):
        self.assertEqual(self.analytics_dashboard.user_count(), 10000)

    def test_brand_count(self):
        self.assertEqual(self.analytics_dashboard.brand_count(), 5000)

    def test_match_count(self):
        self.assertEqual(self.analytics_dashboard.match_count(), 2000)

    def test_email_count(self):
        self.assertEqual(self.analytics_dashboard.email_count(), 1500)

    def test_response_count(self):
        self.assertEqual(self.analytics_dashboard.response_count(), 1200)

    def test_key_performance_metrics(self):
        kpi = self.analytics_dashboard.key_performance_metrics()
        self.assertEqual(kpi['user_growth_rate'], 0.2)
        self.assertEqual(kpi['brand_growth_rate'], 0.1)
        self.assertEqual(kpi['match_rate'], 0.4)
        self.assertEqual(kpi['email_open_rate'], 0.5)
        self.assertEqual(kpi['response_rate'], 0.8)

if __name__ == '__main__':
    unittest.main()