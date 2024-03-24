from testing_setup import FlaskTests
import pytest


class Test_Users(FlaskTests):

    def test_user_crud(self):
        response = self.client.post("/create_user", query_string={
            "username": "joe17",
            "email": "joe@bu.edu",
            "age": "24",
            "first_name": "Joe",
            "last_name": "Smith"
        })
        user_id = response.json['user_id']
        # Store the created user_id for subsequent tests
        assert response.status_code == 201

        response = self.client.get(f"/get_user?user_id={user_id}")
        assert response.status_code == 200
        assert response.json['username'] == 'joe17'
        assert response.json['email'] == 'joe@bu.edu'
        assert response.json['age'] == 24
        assert response.json['firstname'] == 'Joe'
        assert response.json['lastname'] == 'Smith'

        response = self.client.put("/update_user", query_string={
            "user_id": user_id,
            "username": "new_joe",
            "age": "25"
        })
        assert response.status_code == 200

        # Check if the user details have been updated
        response = self.client.get(f"/get_user?user_id={user_id}")
        assert response.status_code == 200
        assert response.json['username'] == 'new_joe'
        assert response.json['age'] == 25

        response = self.client.delete(f"/delete_user?user_id={user_id}")
        assert response.status_code == 200

        # Ensure the user is deleted
        response = self.client.get(f"/get_user?user_id={user_id}")
        assert response.status_code == 404
