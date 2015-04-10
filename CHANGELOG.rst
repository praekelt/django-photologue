Changelog
=========

2.10.3
------
#. Slugify filenames so we never run into filesystem specific issues.

2.10.2
------
#. Defensive code so delete never raises.
#. Do not destroy scale cache if image does not change.

2.10.1
------
#. Change version naming so modern pip does not break.

2.10.praekelt
-------------
#. Defensive code in `create_size` so it never raises.
#. Change product name to `django-photologue-praekelt` so it can be released to Pypi. It is a drop-in replacement for `django-photologue`.

2.9.praekelt
------------
#. Normalize filenames to ASCII.

2.8.praekelt
------------
#. Deprecate `add_accessor_methods` in favour of lazy loading since it did not scale.

