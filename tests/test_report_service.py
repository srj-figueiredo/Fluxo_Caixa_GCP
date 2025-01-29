import unittest
from app import app
import json

class ReportServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_generate_report_success(self):
        response = self.client.get('/generate_report?start_date=2022-01-01&end_date=2022-01-31')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Report generated', str(response.data))

if __name__ == '__main__':
    unittest.main()
