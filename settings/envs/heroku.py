from .production import Production


class Heroku(Production):
    """
    Specific environment configuration for Heroku
    """

    # Append the Whitenoise middleware right after `SecurityMiddleware`
    MIDDLEWARE = Production.MIDDLEWARE.copy()
    MIDDLEWARE.insert(
        MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1,
        'whitenoise.middleware.WhiteNoiseMiddleware'
    )
