import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id):  # noqa: E501
    """delete_user

    deletes a single user based on the ID supplied # noqa: E501

    :param user_id: ID of user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def find_user_by_id(user_id):  # noqa: E501
    """find_user_by_id

    Returns a user based on a single ID, if the user does not have access to the user # noqa: E501

    :param user_id: ID of user
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def update_user(user_id, body=None):  # noqa: E501
    """update_user

    Update user with User ID supplied # noqa: E501

    :param user_id: ID of user
    :type user_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
