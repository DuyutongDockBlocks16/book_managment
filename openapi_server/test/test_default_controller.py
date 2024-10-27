import unittest

from flask import json

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.success import Success  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        Create a new book
        """
        book = {"author":"author","isbn":"isbn","name":"name","rating":0.40041409523050575,"id":"id","publish_date":"2000-01-23T04:56:07.000+00:00"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1/book',
            method='POST',
            headers=headers,
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book(self):
        """Test case for delete_book

        Delete a book by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/book/{book_id}'.format(book_id='book_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        Retrieve a book by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/book/{book_id}'.format(book_id='book_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_books(self):
        """Test case for get_books

        Retrieve a list of books
        """
        query_string = [('author', 'author_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/books',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book(self):
        """Test case for update_book

        Update a book by ID
        """
        book = {"author":"author","isbn":"isbn","name":"name","rating":0.40041409523050575,"id":"id","publish_date":"2000-01-23T04:56:07.000+00:00"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v1/book/{book_id}'.format(book_id='book_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
