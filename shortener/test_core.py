import unittest
from core import app
from config import TestConfig

class CoreTest(unittest.TestCase):
    routes = None
    # Pre-test setup
    def setUp(self):
        self.alias = "qsepu"

        self.app = app # Provide app to the entire test suite
        self.app.config.from_object(TestConfig)

        self.client = self.app.test_client()

        # Disable sending emails during unit testing
        #self.assertEqual(self.client.debug, False)

    # Post-test tear down
    def tearDown(self):
        pass

    def test_url_hashing(self):

        with self.app.app_context():
            from routes import create_url_hash
            url_hash = create_url_hash("https://example.com", "172.0.0.1")

            self.assertEqual(url_hash, "cjbuq")

    def test_create_url(self):
        data = {"url": "https://example.com"}
        response = self.client.post("/url", json=data, follow_redirects=True)

        expected_value = {
            "alias": self.alias,
            "url": "https://example.com"
        }

        self.assertEqual(response.get_json(), expected_value)

    def test_get_url_by_alias(self):
        from routes import get_url_by_alias

        url = get_url_by_alias(self.alias)
        self.assertEqual(url, "https://example.com")

    def test_get_url_info(self):
        response = self.client.get("/url/" + self.alias, follow_redirects=True)

        expected_value = {
            "alias": self.alias,
            "url": "https://example.com"
        }

        self.assertEqual(response.get_json(), expected_value)

    def test_get_url_info_bad(self):
        response = self.client.get("/url/" + self.alias + "bad", follow_redirects=True)

        self.assertEqual(response.get_json(), "Error: no url found")

    def test_redirect(self):
        response = self.client.get("/" + self.alias, follow_redirects=False)

        self.assertIn(b'Redirecting...', response.data)

if __name__ == "__main__":
    unittest.main()

