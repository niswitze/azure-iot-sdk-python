# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .group_authentication_mechanism import GroupAuthenticationMechanism


class SymmetricKeyGroupAuthenticationMechanism(GroupAuthenticationMechanism):
    """The group symmetric key authentication. Devices in this device group use a
    symmetric key derived from this key.

    All required parameters must be populated in order to send to Azure.

    :param group_authentication_type: Required. Constant filled by server.
    :type group_authentication_type: str
    :param symmetric_key: Required. Symmetric key for the group.
    :type symmetric_key: str
    """

    _validation = {
        "group_authentication_type": {"required": True},
        "symmetric_key": {"required": True},
    }

    _attribute_map = {
        "group_authentication_type": {"key": "groupAuthenticationType", "type": "str"},
        "symmetric_key": {"key": "symmetricKey", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SymmetricKeyGroupAuthenticationMechanism, self).__init__(**kwargs)
        self.symmetric_key = kwargs.get("symmetric_key", None)
        self.group_authentication_type = "SymmetricKeyGroupAuthenticationMechanism"
