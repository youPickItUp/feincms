.. _changelog:

Change log
==========

`Next version`_
~~~~~~~~~~~~~~~


`v1.20.0`_ (2021-03-22)
~~~~~~~~~~~~~~~~~~~~~~~

- Changed ``#main`` to the more specific ``#feincmsmain`` so that it doesn't
  collide with Django's admin panel markup.
- Stopped the JavaScript code from constructing invalid POST action URLs in the
  change form.
- Renamed the main branch to main.
- Switched to a declarative setup.
- Switched to GitHub actions.
- Sorted imports.
- Reformated the JavaScript code using prettier.
- Added Python up to 3.9, Django up to the main branch (the upcoming 4.0) to
  the CI list.


`v1.19.0`_ (2021-03-04)
~~~~~~~~~~~~~~~~~~~~~~~

- Fixed a bug where the thumbnailer would try to save JPEGs as RGBA.
- Reformatted the code using black, again.
- Added Python 3.8, Django 3.1 to the build.
- Added the Django 3.2 `.headers` property to the internal dummy response used
  in the etag request processor.
- Added a workaround for ``AppConfig``-autodiscovery related crashes. (Because
  ``feincms.apps`` now has more meanings). Changed the documentation to prefer
  ``feincms.content.application.models.*`` to ``feincms.apps.*``.
- Updated the TinyMCE CDN URL to an version which doesn't show JavaScript
  alerts.
- Added missing ``on_delete`` values to the django-filer content types.


`v1.18.0`_ (2020-01-21)
~~~~~~~~~~~~~~~~~~~~~~~

- Added a style checking job to the CI matrix.
- Dropped compatibility with Django 1.7.


`v1.17.0`_ (2019-11-21)
~~~~~~~~~~~~~~~~~~~~~~~

- Added compatibility with Django 3.0.


`v1.16.0`_ (2019-02-01)
~~~~~~~~~~~~~~~~~~~~~~~

- Reformatted everything using black.
- Added a fallback import for the ``staticfiles`` template tag library
  which will be gone in Django 3.0.


`v1.15.0`_ (2018-12-21)
~~~~~~~~~~~~~~~~~~~~~~~

- Actually made use of the timeout specified as
  ``FEINCMS_THUMBNAIL_CACHE_TIMEOUT`` instead of the hardcoded value of
  seven days.
- Reverted the deprecation of navigation extension autodiscovery.
- Fixed the item editor JavaScript and HTML to work with Django 2.1's
  updated inlines.
- Fixed ``TranslatedObjectManager.only_language`` to evaluate callables
  before filtering.
- Changed the ``render`` protocol of content types to allow returning a
  tuple of ``(ct_template, ct_context)`` which works the same way as
  `feincms3's template renderers
  <https://feincms3.readthedocs.io/en/latest/guides/rendering.html>`__.


`v1.14.0`_ (2018-08-16)
~~~~~~~~~~~~~~~~~~~~~~~

- Added a central changelog instead of creating release notes per
  release because development is moving more slowly owing to the stable
  nature of FeinCMS.
- Fixed history (revision) form, recover form and breadcrumbs when
  FeinCMS is used with Reversion 2.0.x. This accommodates refactoring
  that took place in `Reversion 1.9 and 2.0
  <https://django-reversion.readthedocs.io/en/stable/changelog.html>`_.
  If you are upgrading Reversion (rather than starting a new project),
  please be aware of the significant interface changes and database
  migrations in that product, and attempt upgrading in a development
  environment before upgrading a live site.
- Added ``install_requires`` back to ``setup.py`` so that dependencies
  are installed automatically again. Note that some combinations of e.g.
  Django and django-mptt are incompatible -- look at the `Travis CI
  build configuration
  <https://github.com/feincms/feincms/blob/master/.travis.yml>`_ to find
  out about supported combinations.
- Fixed a few minor compatibility and performance problems.
- Added a new ``FEINCMS_THUMBNAIL_CACHE_TIMEOUT`` setting which allows
  caching whether a thumb exists instead of calling ``storage.exists()``
  over and over (which might be slow with remote storages).
- Fixed random reordering of applications by using an ordered dictionary
  for apps.
- Increased the length of the caption field for media file translations.
- Fixed ``feincms.contrib.tagging`` to actually work with Django
  versions after 1.9.x.


.. _v1.14.0: https://github.com/feincms/feincms/compare/v1.13.0...v1.14.0
.. _v1.15.0: https://github.com/feincms/feincms/compare/v1.14.0...v1.15.0
.. _v1.16.0: https://github.com/feincms/feincms/compare/v1.15.0...v1.16.0
.. _v1.17.0: https://github.com/feincms/feincms/compare/v1.16.0...v1.17.0
.. _v1.18.0: https://github.com/feincms/feincms/compare/v1.17.0...v1.18.0
.. _v1.19.0: https://github.com/feincms/feincms/compare/v1.18.0...v1.19.0
.. _v1.20.0: https://github.com/feincms/feincms/compare/v1.19.0...v1.20.0
.. _Next version: https://github.com/feincms/feincms/compare/v1.20.0...master
