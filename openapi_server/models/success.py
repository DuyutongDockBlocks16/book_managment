from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Success(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, id=None):  # noqa: E501
        """Success - a model defined in OpenAPI

        :param message: The message of this Success.  # noqa: E501
        :type message: str
        :param id: The id of this Success.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'message': str,
            'id': str
        }

        self.attribute_map = {
            'message': 'message',
            'id': 'id'
        }

        self._message = message
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'Success':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Success of this Success.  # noqa: E501
        :rtype: Success
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this Success.


        :return: The message of this Success.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Success.


        :param message: The message of this Success.
        :type message: str
        """

        self._message = message

    @property
    def id(self) -> str:
        """Gets the id of this Success.


        :return: The id of this Success.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Success.


        :param id: The id of this Success.
        :type id: str
        """

        self._id = id