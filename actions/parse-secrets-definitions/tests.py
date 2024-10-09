import unittest

from main import parse_secret

class TestParseSecret(unittest.TestCase):
    def test_parse_secret(self):
        self.assertEqual(parse_secret("secret_name", "project_name"), "SECRET_NAME:project_name/secret_name")
        self.assertEqual(parse_secret("secret_name/version", "project_name"), "SECRET_NAME:project_name/secret_name/version")
        self.assertEqual(parse_secret("123-456", "project_name"), "123_456:project_name/123-456")
        self.assertEqual(parse_secret("123___123___123", "project_name"), "123_123_123:project_name/123___123___123")

    def test_parse_secret_special(self):
        # FIXME: this test is failing and i dont know why
        self.assertEqual(parse_secret("123&&123()123__123*__*_123", "project_name"), "123_123_123_123:project_name/123&&123()123__123*__*_123")

if __name__ == '__main__':
    unittest.main()