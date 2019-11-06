# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .group_authentication_mechanism_py3 import GroupAuthenticationMechanism


class X509CAGroupAuthenticationMechanism(GroupAuthenticationMechanism):
    """X509 authentication method. Devices in this device group have this signing
    certificate in their certificate chain.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param group_authentication_type: Required. Constant filled by server.
    :type group_authentication_type: str
    :ivar certificate: The signing certificate name.
    :vartype certificate: str
    :ivar certificate_metadata: The signing certificate metadata.
    :vartype certificate_metadata: ~protocol.models.CertificateMetadata
    """

    _validation = {
        "group_authentication_type": {"required": True},
        "certificate": {"readonly": True},
        "certificate_metadata": {"readonly": True},
    }

    _attribute_map = {
        "group_authentication_type": {"key": "groupAuthenticationType", "type": "str"},
        "certificate": {"key": "certificate", "type": "str"},
        "certificate_metadata": {"key": "certificateMetadata", "type": "CertificateMetadata"},
    }

    def __init__(self, **kwargs) -> None:
        super(X509CAGroupAuthenticationMechanism, self).__init__(**kwargs)
        self.certificate = None
        self.certificate_metadata = None
        self.group_authentication_type = "X509CAGroupAuthenticationMechanism"
