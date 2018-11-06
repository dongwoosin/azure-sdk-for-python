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

from msrest.serialization import Model


class HTTPConfiguration(Model):
    """HTTP configuration of the connectivity check.

    :param method: HTTP method. Possible values include: 'Get'
    :type method: str or ~azure.mgmt.network.v2018_07_01.models.HTTPMethod
    :param headers: List of HTTP headers.
    :type headers: list[~azure.mgmt.network.v2018_07_01.models.HTTPHeader]
    :param valid_status_codes: Valid status codes.
    :type valid_status_codes: list[int]
    """

    _attribute_map = {
        'method': {'key': 'method', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[HTTPHeader]'},
        'valid_status_codes': {'key': 'validStatusCodes', 'type': '[int]'},
    }

    def __init__(self, **kwargs):
        super(HTTPConfiguration, self).__init__(**kwargs)
        self.method = kwargs.get('method', None)
        self.headers = kwargs.get('headers', None)
        self.valid_status_codes = kwargs.get('valid_status_codes', None)
