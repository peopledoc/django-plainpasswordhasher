# -*- coding: utf-8 -*-
"""Password hashers."""
from collections import OrderedDict

from django.contrib.auth.hashers import BasePasswordHasher, mask_hash


class PlainPasswordHasher(BasePasswordHasher):
    "Plain password hashing algorithm for tests (DO NOT USE in production)."
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        return '%s$$%s' % (self.algorithm, password)

    def verify(self, password, encoded):
        algorithm, hash = encoded.split('$$', 1)
        assert algorithm == self.algorithm
        return password == hash

    def safe_summary(self, encoded):
        return OrderedDict([
            ('algorithm', self.algorithm),
            ('hash', mask_hash(encoded, show=3)),
        ])
