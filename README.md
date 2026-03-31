# Django Authent Backend

A Django authentication backend for authenticating users against external databases with support for custom password hashers including native bcrypt.

## Features

- **DatabaseBackend**: Custom Django authentication backend that queries an external database for user credentials
- **NativeBcryptPasswordHasher**: Verifies bcrypt hashes from external applications without Django prefixes
- **Django Group Management**: Automatic assignment of Django groups based on user permission levels

## Quick Start

### 1. Add to Django Settings

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'django_flask_authent_backend',
]

AUTHENTICATION_BACKENDS = [
    'django_flask_authent_backend.DatabaseBackend',
]

# Database configuration for external authentication
AUTHENT_DATABASE = 'external_db'  # Named database in DATABASES
AUTHENT_TABLENAME = 'schema.users_table'  # Table/schema with user credentials

# Group mapping for permission levels
AUTHENT_GROUPS_MAPPING = {
    "PATH_MANAGER": 1,
    "TREKKING_MANAGER": 2,
    "EDITOR": 3,
    "READER": 4,
    "EDITOR_TREKKING_MANAGEMENT": 6,
}

# Add password hashers
PASSWORD_HASHERS = [
    'django_flask_authent_backend.NativeBcryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]
```

### 2. Configure External Database

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # ... default database config
    },
    'external_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'external_database',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'external-db.example.com',
        'PORT': '5432',
    }
}
```

### User Permission Levels

The backend uses permission levels to determine user roles:

- **Level 0**: Inactive user (no access)
- **Level 1**: Reader (read-only access)
- **Level 2**: Editor Management
- **Level 3**: Path Manager (staff access)
- **Level 4**: Trekking Manager
- **Level 6+**: Superuser (all permissions)

## Configuration

Required settings:

- `AUTHENT_DATABASE`: Name of the external database (must be configured in `DATABASES`)
- `AUTHENT_TABLENAME`: Table name with user credentials (format: `schema.table_name`)
- `AUTHENT_GROUPS_MAPPING`: Mapping of group names to permission levels

Expected columns in external user table:

- `username`: User's login name
- `first_name`: User's first name
- `last_name`: User's last name
- `email`: User's email address
- `password`: Password hash (bcrypt format)
- `level`: Permission level (integer)

## Password Hashing

### Native Bcrypt

The `NativeBcryptPasswordHasher` allows Django to verify bcrypt hashes from external applications:
