# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create user
        """
        body = User()
        response = self.client.open(
            '/api/v1//user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        
        """
        response = self.client.open(
            '/api/v1//user/{userId}'.format(user_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_user_by_id(self):
        """Test case for find_user_by_id

        
        """
        response = self.client.open(
            '/api/v1//user/{userId}'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        
        """
        body = User()
        response = self.client.open(
            '/api/v1//user/{userId}'.format(user_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
