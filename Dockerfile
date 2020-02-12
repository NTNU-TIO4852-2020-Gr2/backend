FROM python:3.8

WORKDIR /app

# Required files
COPY requirements requirements
COPY src src
COPY res res
#COPY locale locale
COPY templates templates
COPY setup/docker-entrypoint.sh entrypoint.sh
COPY setup/uwsgi.prod.ini uwsgi.ini
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
# I18N DISBALED
#RUN python src/manage.py compilemessages --locale=nb

# Remove temporary config file
RUN rm -f src/settings/local.py

# HTTP
EXPOSE 8080
# uWSGI
EXPOSE 8081

CMD ["/bin/bash", "entrypoint.sh"]
