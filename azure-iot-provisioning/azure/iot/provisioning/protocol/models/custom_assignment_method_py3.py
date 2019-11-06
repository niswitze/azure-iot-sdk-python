# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .assignment_method_py3 import AssignmentMethod


class CustomAssignmentMethod(AssignmentMethod):
    """Devices are provisioned to an IoT hub based on your own custom logic. The
    provisioning service passes information about the device to the logic, and
    the logic returns the desired IoT hub as well as the desired initial
    configuration. We recommend using Azure Functions to host your logic.

    All required parameters must be populated in order to send to Azure.

    :param assignment_type: Required. Constant filled by server.
    :type assignment_type: str
    :param webhook_url: Required. The web hook URL used for IoT Hub assignment
     requests.
    :type webhook_url: str
    :param api_version: Required. The API version of the provisioning service
     types (such as DeviceInfo) sent in the custom assignment request. Minimum
     supported version: \\"2018-09-01-preview\\".
    :type api_version: str
    :param target_hubs: The list of IoT hubs the device(s) in this resource
     can be assigned to.
    :type target_hubs: list[str]
    """

    _validation = {
        "assignment_type": {"required": True},
        "webhook_url": {"required": True},
        "api_version": {"required": True},
    }

    _attribute_map = {
        "assignment_type": {"key": "assignmentType", "type": "str"},
        "webhook_url": {"key": "webhookUrl", "type": "str"},
        "api_version": {"key": "apiVersion", "type": "str"},
        "target_hubs": {"key": "targetHubs", "type": "[str]"},
    }

    def __init__(self, *, webhook_url: str, api_version: str, target_hubs=None, **kwargs) -> None:
        super(CustomAssignmentMethod, self).__init__(**kwargs)
        self.webhook_url = webhook_url
        self.api_version = api_version
        self.target_hubs = target_hubs
        self.assignment_type = "CustomAssignmentMethod"
