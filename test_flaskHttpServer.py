import unittest
import json
from flaskHttpServer import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_subscriber(self):
        response = self.client.post('/add-subscriber',
                                    json={'name': 'Alice', 'URI': 'http://good.site.com'})
        self.assertEqual(response.status_code, 200)

    def test_list_subscribers(self):
        response = self.client.get('/list-subscribers')
        self.assertEqual(response.status_code, 200)

    def test_update_and_notify(self):
        response = self.client.post('/update-and-notify',
                                    json={'subject-update': 'Hello'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
