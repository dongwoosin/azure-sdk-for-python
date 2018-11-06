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


class SignalRUsage(Model):
    """Object that describes a specific usage of SignalR resources.

    :param id: Fully qualified ARM resource id
    :type id: str
    :param current_value: Current value for the usage quota.
    :type current_value: long
    :param limit: The maximum permitted value for the usage quota. If there is
     no limit, this value will be -1.
    :type limit: long
    :param name: Localizable String object containing the name and a localized
     value.
    :type name: ~azure.mgmt.signalr.models.SignalRUsageName
    :param unit: Representing the units of the usage quota. Possible values
     are: Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond.
    :type unit: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'long'},
        'limit': {'key': 'limit', 'type': 'long'},
        'name': {'key': 'name', 'type': 'SignalRUsageName'},
        'unit': {'key': 'unit', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, current_value: int=None, limit: int=None, name=None, unit: str=None, **kwargs) -> None:
        super(SignalRUsage, self).__init__(**kwargs)
        self.id = id
        self.current_value = current_value
        self.limit = limit
        self.name = name
        self.unit = unit
