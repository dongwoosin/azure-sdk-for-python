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


class ReportConfigDefinition(Model):
    """The definition of a report config.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of the report. Default value: "Usage" .
    :vartype type: str
    :param timeframe: The time frame for pulling data for the report. If
     custom, then a specific time period must be provided. Possible values
     include: 'WeekToDate', 'MonthToDate', 'YearToDate', 'Custom'
    :type timeframe: str or ~azure.mgmt.consumption.models.TimeframeType
    :param time_period: Has time period for pulling data for the report.
    :type time_period: ~azure.mgmt.consumption.models.ReportConfigTimePeriod
    :param dataset: Has definition for data in this report config.
    :type dataset: ~azure.mgmt.consumption.models.ReportConfigDataset
    """

    _validation = {
        'type': {'required': True, 'constant': True},
        'timeframe': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'timeframe': {'key': 'timeframe', 'type': 'str'},
        'time_period': {'key': 'timePeriod', 'type': 'ReportConfigTimePeriod'},
        'dataset': {'key': 'dataset', 'type': 'ReportConfigDataset'},
    }

    type = "Usage"

    def __init__(self, timeframe, time_period=None, dataset=None):
        super(ReportConfigDefinition, self).__init__()
        self.timeframe = timeframe
        self.time_period = time_period
        self.dataset = dataset
