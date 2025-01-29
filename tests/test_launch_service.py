import unittest
from app import app
import json

class LaunchServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_launch_value_success(self):
        response = self.client.post('/launch', 
                                    data=json.dumps({'value': 100.0, 'type': 'debit'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Transaction recorded successfully', str(response.data))

    def test_launch_value_invalid(self):
        response = self.client.post('/launch', 
                                    data=json.dumps({'value': -100.0, 'type': 'credit'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid value or type', str(response.data))

if __name__ == '__main__':
    unittest.main()
