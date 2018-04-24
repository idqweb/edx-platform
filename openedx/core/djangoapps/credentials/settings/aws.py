"""Production settings for Credentials"""


def plugin_settings(settings):
    # Credentials Settings
    settings.ACE_ROUTING_KEY = settings.ENV_TOKENS.get('ACE_ROUTING_KEY', settings.ACE_ROUTING_KEY)

    settings.CREDENTIALS_INTERNAL_SERVICE_URL = settings.ENV_TOKENS.get(
        'CREDENTIALS_INTERNAL_SERVICE_URL', settings.CREDENTIALS_INTERNAL_SERVICE_URL
    )
    settings.CREDENTIALS_PUBLIC_SERVICE_URL = settings.ENV_TOKENS.get(
        'CREDENTIALS_PUBLIC_SERVICE_URL', settings.CREDENTIALS_PUBLIC_SERVICE_URL
    )
