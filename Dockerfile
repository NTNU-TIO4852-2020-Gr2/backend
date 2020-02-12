FROM python:3.8

WORKDIR /app

# Required files
COPY src src
COPY files files
COPY locale locale
COPY requirements requirements
COPY templates templates
COPY setup/docker-entrypoint.sh entrypoint.sh
COPY manage.py manage.py
COPY setup/uwsgi.ini uwsgi.ini
RUN mkdir -p log

# Extra files
COPY CHANGELOG.md ./
COPY LICENSE.txt ./
COPY VERSION ./

# Install requirements
RUN apt-get update && apt-get install -y gettext
RUN pip install -r requirements/production.txt --upgrade

# Add temporary config file
COPY setup/local.template.py src/settings/local.py

# Compile translations
RUN python manage.py compilemessages --locale=nb

# Remove temporary config file
RUN rm -f src/settings/local.py

# HTTP
EXPOSE 8080
# uWSGI
EXPOSE 8081

CMD ["/bin/bash", "entrypoint.sh"]
