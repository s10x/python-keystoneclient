# Copyright 2010 Jacob Kaplan-Moss
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Exception definitions.

.. py:exception:: AuthorizationFailure

.. py:exception:: ClientException

.. py:exception:: HttpError

.. py:exception:: ValidationError

.. py:exception:: Unauthorized

"""

from keystoneauth import exceptions as new_exceptions

from keystoneclient.i18n import _


# NOTE(jamielennox): Import only the exceptions we need from keystoneauth. Lots
# of other places read exceptions from keystoneclient and so we need to
# maintain these for backwards compatibility. I'm naming them individually so
# that we don't import a lot of new exceptions and make more compatibility
# issues for ourselves in the future.

ClientException = new_exceptions.ClientException
HttpError = new_exceptions.HttpError
HTTPClientError = new_exceptions.HTTPClientError
BadRequest = new_exceptions.BadRequest
Unauthorized = new_exceptions.Unauthorized
PaymentRequired = new_exceptions.PaymentRequired
Forbidden = new_exceptions.Forbidden
NotFound = new_exceptions.NotFound
MethodNotAllowed = new_exceptions.MethodNotAllowed
NotAcceptable = new_exceptions.NotAcceptable
ProxyAuthenticationRequired = new_exceptions.ProxyAuthenticationRequired
Conflict = new_exceptions.Conflict
Gone = new_exceptions.Gone
LengthRequired = new_exceptions.LengthRequired
PreconditionFailed = new_exceptions.PreconditionFailed
RequestEntityTooLarge = new_exceptions.RequestEntityTooLarge
RequestUriTooLong = new_exceptions.RequestUriTooLong
UnsupportedMediaType = new_exceptions.UnsupportedMediaType
RequestedRangeNotSatisfiable = new_exceptions.RequestedRangeNotSatisfiable
ExpectationFailed = new_exceptions.ExpectationFailed
UnprocessableEntity = new_exceptions.UnprocessableEntity
HttpServerError = new_exceptions.HttpServerError
InternalServerError = new_exceptions.InternalServerError
HttpNotImplemented = new_exceptions.HttpNotImplemented
BadGateway = new_exceptions.BadGateway
ServiceUnavailable = new_exceptions.ServiceUnavailable
GatewayTimeout = new_exceptions.GatewayTimeout
HttpVersionNotSupported = new_exceptions.HttpVersionNotSupported
from_response = new_exceptions.from_response


# NOTE(jamielennox): Rahh! this is just wrong. In the apiclient conversion
# someone mapped the connection timeout onto the HTTP timeout exception. Assume
# people want the connection timeout as this is much more common.
RequestTimeout = new_exceptions.ConnectTimeout

ConnectionError = new_exceptions.ConnectionError
SSLError = new_exceptions.SSLError
Timeout = new_exceptions.ConnectTimeout


# NOTE(akurilin): This alias should be left here to support backwards
# compatibility until we are sure that usage of these exceptions in
# projects is correct.
ConnectionRefused = ConnectionError
HTTPNotImplemented = HttpNotImplemented
Timeout = RequestTimeout
HTTPError = HttpError


class HTTPRedirection(HttpError):
    """HTTP Redirection."""
    message = _("HTTP Redirection")


class MultipleChoices(HTTPRedirection):
    """HTTP 300 - Multiple Choices.

    Indicates multiple options for the resource that the client may follow.
    """

    http_status = 300
    message = _("Multiple Choices")


class ValidationError(ClientException):
    """Error in validation on API client side."""


class UnsupportedVersion(ClientException):
    """User is trying to use an unsupported version of the API."""


class CommandError(ClientException):
    """Error in CLI tool."""


AuthorizationFailure = new_exceptions.AuthorizationFailure


class AuthPluginOptionsMissing(AuthorizationFailure):
    """Auth plugin misses some options."""
    def __init__(self, opt_names):
        super(AuthPluginOptionsMissing, self).__init__(
            _("Authentication failed. Missing options: %s") %
            ", ".join(opt_names))
        self.opt_names = opt_names


class AuthSystemNotFound(AuthorizationFailure):
    """User has specified an AuthSystem that is not installed."""
    def __init__(self, auth_system):
        super(AuthSystemNotFound, self).__init__(
            _("AuthSystemNotFound: %s") % repr(auth_system))
        self.auth_system = auth_system


class CertificateConfigError(Exception):
    """Error reading the certificate."""
    def __init__(self, output):
        self.output = output
        msg = _('Unable to load certificate.')
        super(CertificateConfigError, self).__init__(msg)


class CMSError(Exception):
    """Error reading the certificate."""
    def __init__(self, output):
        self.output = output
        msg = _('Unable to sign or verify data.')
        super(CMSError, self).__init__(msg)


EndpointException = new_exceptions.CatalogException
EmptyCatalog = new_exceptions.EmptyCatalog
EndpointNotFound = new_exceptions.EndpointNotFound


class NoUniqueMatch(EndpointException):
    """Multiple entities found instead of one."""
    pass


class AmbiguousEndpoints(EndpointException):
    """Found more than one matching endpoint in Service Catalog."""
    def __init__(self, endpoints=None):
        super(AmbiguousEndpoints, self).__init__(
            _("AmbiguousEndpoints: %s") % repr(endpoints))
        self.endpoints = endpoints


DiscoveryFailure = new_exceptions.DiscoveryFailure
VersionNotAvailable = new_exceptions.VersionNotAvailable


class MethodNotImplemented(ClientException):
    """Method not implemented by the keystoneclient API."""


MissingAuthPlugin = new_exceptions.MissingAuthPlugin
NoMatchingPlugin = new_exceptions.NoMatchingPlugin
InvalidResponse = new_exceptions.InvalidResponse
