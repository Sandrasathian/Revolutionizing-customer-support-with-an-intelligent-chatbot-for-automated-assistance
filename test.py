import unittest
from chatbot.bot import get_response  # Adjust this import path based on your project structure

class TestChatbotResponses(unittest.TestCase):

    def test_greeting(self):
        response = get_response("Hello")
        self.assertIn(response.lower(), ["hi there!", "hello!", "how can i help you?"])

    def test_farewell(self):
        response = get_response("Bye")
        self.assertIn("bye", response.lower())

    def test_order_status(self):
        response = get_response("Where is my order?")
        self.assertTrue(any(word in response.lower() for word in ["order", "tracking", "status"]))

    def test_unknown_input(self):
        response = get_response("Blah blah blurb")
        self.assertIn("sorry", response.lower())

    def test_case_insensitivity(self):
        response_upper = get_response("HELLO")
        response_lower = get_response("hello")
        self.assertEqual(response_upper, response_lower)

if _name_ == '_main_':
    unittest.main()
