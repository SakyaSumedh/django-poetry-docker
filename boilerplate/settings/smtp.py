from decouple import config

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
FROM_EMAIL = config("FROM_EMAIL", default="info@boilerplate.com")
EMAIL_HOST = config("EMAIL_HOST", default="")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_PORT = config("EMAIL_PORT", default=587)
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 5

EMAIL_SUBJECT_PREFIX = config("EMAIL_SUBJECT_PREFIX", default="[BoilerPlate]")
