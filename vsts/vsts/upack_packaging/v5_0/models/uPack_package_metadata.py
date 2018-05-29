# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class UPackPackageMetadata(Model):
    """UPackPackageMetadata.

    :param super_root_id:
    :type super_root_id: str
    :param description:
    :type description: str
    :param manifest_id:
    :type manifest_id: str
    """

    _attribute_map = {
        'super_root_id': {'key': 'superRootId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'manifest_id': {'key': 'manifestId', 'type': 'str'}
    }

    def __init__(self, super_root_id=None, description=None, manifest_id=None):
        super(UPackPackageMetadata, self).__init__()
        self.super_root_id = super_root_id
        self.description = description
        self.manifest_id = manifest_id
