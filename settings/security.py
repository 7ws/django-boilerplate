from configurations import values


class SecuritySettings:
    """
    Security-related Django settings
    """

    ALLOWED_HOSTS = values.ListValue(default=[])

    SECRET_KEY = values.SecretValue()
