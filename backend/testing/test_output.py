import unittest
from ..flask_factory import create_flask_app


class FlaskBookshelfTests(unittest.TestCase): 

    flask_app = None

    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
            # creates a test client
            self.flaskapp = create_flask_app()
            # propagate the exceptions to the test client
            self.flaskapp.testing = True

    def tearDown(self):
            pass

    def test1(self):
            result = self.flaskapp.get('/')

            self.assertEqual(result.status_code, 200) 