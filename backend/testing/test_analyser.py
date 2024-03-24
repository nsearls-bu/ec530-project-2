from testing_setup import FlaskTests
import pytest
from io import BytesIO
from uuid import UUID, uuid4
import time
class Test_Analyser(FlaskTests):

    def test_user_uploading(self):
        data = {}
        data['file'] = (BytesIO(b"Hello"), 'test.txt')
        response = self.client.post("/create_document", data=data, content_type='multipart/form-data',)
        # First upload a document
        assert response.status_code == 201
        document_id = response.json['document_id']
        response = self.client.post("/create_user", query_string={
            "username": "joe17",
            "email": "joe@bu.edu",
            "age": "24",
            "first_name": "Joe",
            "last_name": "Smith"
        })
        user_id = response.json['user_id']
        assert response.status_code == 201
        assert isinstance(UUID(user_id), UUID)
        response = self.client.post("/create_response", query_string={
            "user_id" : user_id,
            "document_id" : document_id
        })
        assert response.status_code == 201

        task_id = response.json['summary_task']['task_id']
        time.sleep(6)
        response = self.client.get(f"/results/{task_id}")
        assert (response.json['output'] == "We've processed this data")
