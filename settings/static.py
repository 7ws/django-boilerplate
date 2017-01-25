from configurations import values

from .base import BASE_DIR


class StaticMedia:
    """
    Configuration for front-end assets
    """

    # URLs
    STATIC_URL = values.Value('/static/')
    MEDIA_URL = values.Value('/media/')

    # Main directories
    STATIC_ROOT = values.PathValue(BASE_DIR / '_static', check_exists=False)
    MEDIA_ROOT = values.PathValue(BASE_DIR / '_media', check_exists=False)

    # Finders
    STATICFILES_DIRS = [
    ]
