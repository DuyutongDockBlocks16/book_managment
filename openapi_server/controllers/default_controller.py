import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.success import Success  # noqa: E501
from openapi_server import util


def create_book(book):  # noqa: E501
    """Create a new book

     # noqa: E501

    :param book: 
    :type book: dict | bytes

    :rtype: Union[Success, Tuple[Success, int], Tuple[Success, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book(book_id):  # noqa: E501
    """Delete a book by ID

     # noqa: E501

    :param book_id: ID of the book to delete
    :type book_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_book_by_id(book_id):  # noqa: E501
    """Retrieve a book by ID

     # noqa: E501

    :param book_id: ID of the book to retrieve
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_books(author=None):  # noqa: E501
    """Retrieve a list of books

     # noqa: E501

    :param author: Filter books by author name
    :type author: str

    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_book(book_id, book):  # noqa: E501
    """Update a book by ID

     # noqa: E501

    :param book_id: ID of the book to update
    :type book_id: str
    :param book: 
    :type book: dict | bytes

    :rtype: Union[Success, Tuple[Success, int], Tuple[Success, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
