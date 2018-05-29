# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PackageVersionDetails(Model):
    """PackageVersionDetails.

    :param views: The view to which the package version will be added
    :type views: :class:`JsonPatchOperation <uPack.v5_0.models.JsonPatchOperation>`
    """

    _attribute_map = {
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, views=None):
        super(PackageVersionDetails, self).__init__()
        self.views = views
