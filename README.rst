**WARNING: this project is not maintained**

##########################
django-plainpasswordhasher
##########################

Dummy (plain text) password hashing for Django... for use in tests!


***************
Speed up tests!
***************

Cryptography is greedy. When you run tests, you usually do not care about
password security, but you care about performances. Using dummy password
hashing speeds up tests!

Install ``django-plainpasswordhasher`` with your favorite installer.
Here is an example using pip:

.. code:: sh

   pip install django-plainpasswordhasher

Then configure your test settings:

.. code:: python

   PASSWORD_HASHERS = ('django_plainpasswordhasher.PlainPasswordHasher', )


**************************************
Except explicit password hashing tests
**************************************

In most cases, using a dummy password hasher will do the job.
But you may write some tests that require real password hashing. In such a
case, let's override settings!

.. code:: python

   from django.conf import global_settings  # Django default settings...
                                            # You may use your project's
                                            # default settings instead.
   from django.test import TestCase
   from django.test.utils import override_settings

   @override_settings(PASSWORD_HASHERS=global_settings.PASSWORD_HASHERS)
   class CryptographyTestCase(TestCase):
	"""Tests that require real cryptography."""


*********
Resources
*********

* PyPI page: https://pypi.python.org/pypi/django-plainpasswordhasher
* Code repository: https://github.com/novapost/django-plainpasswordhasher
* Bugtracker: https://github.com/novapost/django-plainpasswordhasher/issues
* Continuous integration: https://travis-ci.org/novapost/django-plainpasswordhasher


**********
References
**********

* `Original blog post
  <http://tech.novapost.fr/django-comment-booster-ses-tests-en-1-minute.html>`_

* `Django 1.5 documentation about getting faster tests
  <https://docs.djangoproject.com/en/1.5/topics/testing/#speeding-up-the-tests>`_ 

* `Discussion about password hashers & testing in Django issues
  <https://code.djangoproject.com/ticket/20917>`_
