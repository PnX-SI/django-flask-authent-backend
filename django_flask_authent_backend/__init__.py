"""Django authentication backend for external databases."""

__version__ = "0.1.0"
__author__ = "Parc national des ecrins"

from .backend import DatabaseBackend
from .hashers import NativeBcryptPasswordHasher

__all__ = [
    "DatabaseBackend",
    "NativeBcryptPasswordHasher",
]
