# -*- coding: utf-8 -*-
"""Tests."""
import unittest


class APITestCase(unittest.TestCase):
    """Test suite around :mod:`django_plainpasswordhasher` attributes.

    Mostly prevents unplanned backward incompatibilities.

    """
    def test_plainpasswordhasher(self):
        """Import PlainPasswordHasher from django_plainpasswordhasher."""
        from django_plainpasswordhasher import PlainPasswordHasher  # NoQA
