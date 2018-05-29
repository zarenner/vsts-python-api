# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class UPackApiClient(VssClient):
    """UPackApi
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(UPackApiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'd397749b-f115-4027-b6dd-77a65dd10d21'

    def update_package_versions(self, batch_request, feed_id):
        """UpdatePackageVersions.
        [Preview API] Update several packages from a single feed in a single request. The updates to the packages do not happen atomically.
        :param :class:`<UPackPackagesBatchRequest> <uPack-api.v5_0.models.UPackPackagesBatchRequest>` batch_request: Information about the packages to update, the operation to perform, and its associated data.
        :param str feed_id: Feed which contains the packages to update.
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(batch_request, 'UPackPackagesBatchRequest')
        self._send(http_method='POST',
                   location_id='c17e81ae-4caa-4d8b-a431-6b329e890281',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version_from_recycle_bin(self, feed_id, package_name, package_version):
        """DeletePackageVersionFromRecycleBin.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        self._send(http_method='DELETE',
                   location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                   version='5.0-preview.1',
                   route_values=route_values)

    def get_package_version_metadata_from_recycle_bin(self, feed_id, package_name, package_version):
        """GetPackageVersionMetadataFromRecycleBin.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :rtype: :class:`<UPackPackageVersionDeletionState> <uPack-api.v5_0.models.UPackPackageVersionDeletionState>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='GET',
                              location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('UPackPackageVersionDeletionState', response)

    def restore_package_version_from_recycle_bin(self, package_version_details, feed_id, package_name, package_version):
        """RestorePackageVersionFromRecycleBin.
        [Preview API]
        :param :class:`<UPackRecycleBinPackageVersionDetails> <uPack-api.v5_0.models.UPackRecycleBinPackageVersionDetails>` package_version_details:
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'UPackRecycleBinPackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='3ba455ae-31e6-409e-849f-56c66888d004',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

    def delete_package_version(self, feed_id, package_name, package_version):
        """DeletePackageVersion.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :rtype: :class:`<Package> <uPack-api.v5_0.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        response = self._send(http_method='DELETE',
                              location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('Package', response)

    def get_package_version(self, feed_id, package_name, package_version, show_deleted=None):
        """GetPackageVersion.
        [Preview API]
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        :param bool show_deleted:
        :rtype: :class:`<Package> <uPack-api.v5_0.models.Package>`
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        query_parameters = {}
        if show_deleted is not None:
            query_parameters['showDeleted'] = self._serialize.query('show_deleted', show_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                              version='5.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def update_package_version(self, package_version_details, feed_id, package_name, package_version):
        """UpdatePackageVersion.
        [Preview API]
        :param :class:`<PackageVersionDetails> <uPack-api.v5_0.models.PackageVersionDetails>` package_version_details:
        :param str feed_id:
        :param str package_name:
        :param str package_version:
        """
        route_values = {}
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_name is not None:
            route_values['packageName'] = self._serialize.url('package_name', package_name, 'str')
        if package_version is not None:
            route_values['packageVersion'] = self._serialize.url('package_version', package_version, 'str')
        content = self._serialize.body(package_version_details, 'PackageVersionDetails')
        self._send(http_method='PATCH',
                   location_id='72f61ca4-e07c-4eca-be75-6c0b2f3f4051',
                   version='5.0-preview.1',
                   route_values=route_values,
                   content=content)

