# -*- coding: utf-8 -*-
"""Dummy (plain text) password hashing for Django... for use in tests!"""
import pkg_resources


#: Module version, as defined in PEP-0396.
__version__ = pkg_resources.get_distribution(__package__).version


# API shortcuts.
from django_plainpasswordhasher.hashers import PlainPasswordHasher  # NoQA
