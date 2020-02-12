# Docker Image

The Docker images are the intended way to run this application stack.

## Environment Variables

* `APP_UID=<uid>`: UID to use for the `app` user. Has effect only for the first start of the container.
* `APP_GID=<gid>`: Same as `APP_UID`, but for GID.
* `SUPERUSER_USERNAME=<username>`: If set, a superuser with the specified username is attempted created if a user with the specified username does not yet exist. `SUPERUSER_USERNAME`, `SUPERUSER_USERNAME` and `SUPERUSER_USERNAME` adds the superuser to the database, and can be removed after being set for one application start.
* `SUPERUSER_EMAIL=<email>`: Email address for the superuser to be created. Required if `SUPERUSER_USERNAME` is set and the user does not exist yet.
* `SUPERUSER_PASSWORD=<password>`: Password for the superuser to be created. Required if `SUPERUSER_USERNAME` is set and the user does not exist yet.
* `SUPERUSER_INACTIVE=[true]` (default: false): Deactivates the superuser if it was just created. (`User.is_active` is set to false.)
* `NO_START=[true]`: If the uWSGI server should start or not at the end of the entrypoint script.

## Internal Directories and Files

* `/app/src/settings/local.py`: (Required) Settings file for the Django app.
* `/app/log`: Log directory for the uWSGI server hosting the Django app.
* `/app/static`: Where static files are collected to on application start. Can be mounted to serve static files directly from reverse proxy.
* `/app/db.sqlite3`: Example location for SQLite database, if configured to use it. The actual path depends on what is configured in the `local.py` config.
