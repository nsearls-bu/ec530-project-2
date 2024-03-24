from testing_setup import FlaskTests


class Test_Output(FlaskTests):


    def test_get_responses(self):
        response = self.client.get("/get_responses", query_string={'user_id': 1, "document_id": 1})
        assert response.status_code == 404
