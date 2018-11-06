# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource_py3 import ProxyOnlyResource


class Deployment(ProxyOnlyResource):
    """User crendentials used for publishing activity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param status: Deployment status.
    :type status: int
    :param message: Details about deployment status.
    :type message: str
    :param author: Who authored the deployment.
    :type author: str
    :param deployer: Who performed the deployment.
    :type deployer: str
    :param author_email: Author email.
    :type author_email: str
    :param start_time: Start time.
    :type start_time: datetime
    :param end_time: End time.
    :type end_time: datetime
    :param active: True if deployment is currently active, false if completed
     and null if not started.
    :type active: bool
    :param details: Details on deployment.
    :type details: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'int'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'deployer': {'key': 'properties.deployer', 'type': 'str'},
        'author_email': {'key': 'properties.author_email', 'type': 'str'},
        'start_time': {'key': 'properties.start_time', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.end_time', 'type': 'iso-8601'},
        'active': {'key': 'properties.active', 'type': 'bool'},
        'details': {'key': 'properties.details', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, status: int=None, message: str=None, author: str=None, deployer: str=None, author_email: str=None, start_time=None, end_time=None, active: bool=None, details: str=None, **kwargs) -> None:
        super(Deployment, self).__init__(kind=kind, **kwargs)
        self.status = status
        self.message = message
        self.author = author
        self.deployer = deployer
        self.author_email = author_email
        self.start_time = start_time
        self.end_time = end_time
        self.active = active
        self.details = details
