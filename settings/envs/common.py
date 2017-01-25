from configurations import Configuration, values
import dj_database_url
import dj_email_url

from .. import auth, base, security, static


class Common(
    auth.AuthenticationSettings,
    base.DjangoOverrides,
    security.SecuritySettings,
    static.StaticMedia,
    Configuration,
):
    """
    Custom settings that are likely to be common among environments
    """

    DATABASE_URL = values.Value(
        f'sqlite:///{base.BASE_DIR / "db.sqlite"}',
        environ_name='DATABASE_URL',
        environ_prefix='',
    )
    DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

    EMAIL_URL = values.Value(
        'console://',
        environ_name='EMAIL_URL',
        environ_prefix='',
    )
    vars().update(dj_email_url.parse(EMAIL_URL))  # Load EMAIL_* into the class

    LANGUAGE_CODE = 'en-us'
