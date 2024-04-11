from testing_setup import FlaskTests
import pytest
from io import BytesIO
from uuid import UUID, uuid4
import time
class Test_Analyser(FlaskTests):
    def test_user_injection(self):
        data = {}
        data['file'] = (BytesIO(b"--"), 'test.txt')
        # Test with SQL comment. This should make the code crash if not properly sanitized.
        response = self.client.post("/create_document", data=data, content_type='multipart/form-data',)
        assert response.status_code == 201

        response = self.client.post("/create_user", query_string={
            "username": "; DROP TABLE USERS",
            "email": "joe@bu.edu",
            "age": "24",
            "first_name": "Joe",
            "last_name": "Smith"
        })
        assert response.status_code == 201

