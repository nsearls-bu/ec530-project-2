from testing_setup import FlaskTests
import pytest
from io import BytesIO

class Test_Uploader(FlaskTests):

    def test_user_uploading(self):
        data = {}
        data['file'] = (BytesIO(b"abcdef"), 'test.txt')
        response = self.client.post("/create_document", data=data, content_type='multipart/form-data',)
        assert response.status_code == 201

