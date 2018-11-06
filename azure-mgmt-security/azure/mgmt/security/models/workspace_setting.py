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

from .resource import Resource


class WorkspaceSetting(Resource):
    """Configures where to store the OMS agent data for workspaces under a scope.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param workspace_id: Required. The full Azure ID of the workspace to save
     the data in
    :type workspace_id: str
    :param scope: Required. All the VMs in this scope will send their security
     data to the mentioned workspace unless overridden by a setting with more
     specific scope
    :type scope: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'workspace_id': {'required': True},
        'scope': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WorkspaceSetting, self).__init__(**kwargs)
        self.workspace_id = kwargs.get('workspace_id', None)
        self.scope = kwargs.get('scope', None)
