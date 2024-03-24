import unittest
from flask_factory import create_flask_app


class FlaskTests(unittest.TestCase): 
    '''Parent class for flask testing'''

    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
            # creates a test client
            app = create_flask_app()
            # propagate the exceptions to the test client
            self.ctx = app.app_context()
            self.ctx.push()
            self.client = app.test_client()



