from configurations import values

from .common import Common


class UnitTest(Common):
    """
    Special settings used for tests only
    """

    DATABASES = values.DatabaseURLValue('sqlite:///:memory:')
    SECRET_KEY = 'super-secret!'
