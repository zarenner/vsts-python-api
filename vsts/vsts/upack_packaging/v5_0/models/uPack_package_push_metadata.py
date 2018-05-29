# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .uPack_package_metadata import UPackPackageMetadata


class UPackPackagePushMetadata(UPackPackageMetadata):
    """UPackPackagePushMetadata.

    :param super_root_id:
    :type super_root_id: str
    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    :param proof_nodes:
    :type proof_nodes: list of str
    """

    _attribute_map = {
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'},
        'proof_nodes': {'key': 'proofNodes', 'type': '[str]'}
    }

    def __init__(self, super_root_id=None, description=None, manifest_id=None, proof_nodes=None):
        super(UPackPackagePushMetadata, self).__init__(super_root_id=super_root_id, description=description, manifest_id=manifest_id)
        self.proof_nodes = proof_nodes
