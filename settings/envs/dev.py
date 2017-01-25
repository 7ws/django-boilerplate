from configurations import values

from .common import Common


class Development(Common):
    """
    Settings for local development environments
    """

    ALLOWED_HOSTS = values.ListValue(['*'])

    DEBUG = values.BooleanValue(True)

    INTERNAL_IPS = ['127.0.0.1', '::1']
