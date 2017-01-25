from configurations import values


class AuthenticationSettings:
    """
    Settings related to authentication throughout all apps
    """

    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': f'django.contrib.auth.password_validation.{name}'}
        for name in [
            'UserAttributeSimilarityValidator',
            'MinimumLengthValidator',
            'CommonPasswordValidator',
            'NumericPasswordValidator',
        ]
    ]
