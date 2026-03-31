"""
Example Django settings configuration for django-authent-backend
"""

# Add to INSTALLED_APPS
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_flask_authent_backend",
]


# Group permission level mapping
AUTHENT_GROUPS_MAPPING = {
    "PATH_MANAGER": 1,
    "TREKKING_MANAGER": 2,
    "EDITOR": 3,
    "READER": 4,
    "EDITOR_TREKKING_MANAGEMENT": 6,
}

# External authentication database configuration
AUTHENT_DATABASE = "external_auth_db"
AUTHENT_TABLENAME = "auth.users"

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
    "external_auth_db": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "external_db",
        "USER": "db_user",
        "PASSWORD": "db_password",
        "HOST": "localhost",
        "PORT": "5432",
    },
}

# Authentication backend
AUTHENTICATION_BACKENDS = [
    "django_flask_authent_backend.DatabaseBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Password hashers - order matters!
PASSWORD_HASHERS = [
    "django_flask_authent_backend.NativeBcryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
