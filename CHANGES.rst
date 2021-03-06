Flask-JWT Changelog
===================

Here you can see the full list of changes between each Flask-JWT release.

Version 0.4
-----------

Released on March 27th 2017

- Add role check by Aurélien Lajoie
  https://github.com/webstack/flask-jwt/pull/4

Version 0.3.4
-------------

Released on March 24th 2017

- Remove logging of errors by Jean-Philippe Morin
  https://github.com/webstack/flask-jwt/pull/2

Version 0.3.3
-------------

Released on August 8th 2016

.. note:: Forked by Webstack

- One One PR to rule them all
  https://github.com/mattupstate/flask-jwt/pull/95

Version 0.3.2
-------------

Released on November 3rd 2015

- Fixed an Authorization header conditional bug

Version 0.3.1
-------------

Released on October 26th 2015

- Fix a bug with `auth_request_handler`
- Deprecate `auth_request_handler`

Version 0.3.0
-------------

Released on October 15th 2015

.. note:: This release includes many breaking changes

- Fix major implementation issue with encoding/decoding tokens
- Changed new configuration options to align with PyJWT
- Changed `current_user` to `current_identity`

Version 0.2.0
-------------

Released on June 10th 2014

- Fixed an issue where `current_user` was not None
- Added a response handler hook to be able to adjust auth response(s)
- Removed the configurable handlers in favor of decorators
- Removed pyjwt dependency


Version 0.1.0
-------------

Released on March 5th 2014

- Initial release
