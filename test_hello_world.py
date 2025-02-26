import hello_world
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(hello_world.greet(), greeting)
        print("Today is AI DAY")
        print(1)
        print(2)
        print(3)
        print(4)
        print(5)
        print(6)
        #--------------new branch-------------
        print(7)
        print(8)

if __name__ == '__main__':
    unittest.main()