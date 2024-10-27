import connexion
from typing import Dict, List, Tuple, Union

from openapi_server.models import Error, Success
from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.success import Success  # noqa: E501
from openapi_server import util

# 模拟数据库
books_db = {}
book_counter = 1  # 用于生成唯一的书籍 ID


def create_book() -> tuple[Success, int] | tuple[Error, int]:
    """Create a new book
    """
    global book_counter  # 引用全局变量
    if connexion.request.is_json:
        book_data = Book.from_dict(connexion.request.get_json())  # 转换请求数据为 Book 对象
        book_id = str(book_counter)  # 生成新的 ID
        book_counter += 1  # 增加 ID 计数
        book_data.id = book_id  # 设置 ID
        books_db[book_id] = book_data  # 保存到模拟数据库ji
        return Success(id=book_id, message="Book successfully created"), 201
    return Error(message="Request body must be JSON"), 422


def delete_book(book_id: str) -> Union[None, Tuple[None, int]]:
    """Delete a book by ID
    """
    if book_id in books_db:
        del books_db[book_id]  # 从模拟数据库中删除书籍
        return None, 204  # 返回无内容的响应
    return Error(message="Book not found"), 404


def get_book_by_id(book_id: str) -> Union[Book, Tuple[Book, int]]:
    """Retrieve a book by ID
    """
    if book_id in books_db:
        return books_db[book_id], 200  # 返回书籍对象和200状态码
    return Error(message="Book not found"), 404


def get_books(author=None) -> Union[List[Book], Tuple[List[Book], int]]:
    """Retrieve a list of books
    """
    if author:
        # 根据作者过滤书籍
        filtered_books = [book for book in books_db.values() if book.author == author]
        if len(filtered_books) == 0:
            return Error(message="Book not found"), 404
        return filtered_books, 200
    return list(books_db.values()), 200  # 返回所有书籍


def update_book(book_id: str) -> Union[Success, Tuple[Success, int]]:
    """Update a book by ID
    """
    if book_id in books_db:
        if connexion.request.is_json:
            book_data = Book.from_dict(connexion.request.get_json())
            book_data.id = book_id  # 保持 ID 不变
            books_db[book_id] = book_data  # 更新书籍
            return Success(id=book_id, message="Book successfully updated"), 200
    return Error(message="Book not found"), 404
