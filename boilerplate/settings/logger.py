# Logging configurations
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} {module} {levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/boilerplate.log",
            "when": "midnight",
            "backupCount": 50,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "project": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
