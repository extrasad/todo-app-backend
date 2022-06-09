FROM python:3.7-alpine3.10

# Default directory for all stages
WORKDIR /app

# Default env
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1
ENV GRPC_PYTHON_BUILD_SYSTEM_OPENSSL 1
ENV GRPC_PYTHON_BUILD_SYSTEM_ZLIB 1

RUN apk update
# psycopg2 dependencies
RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache postgresql-dev
# Pillow dependencies
RUN apk add --no-cache jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev bash
# CFFI dependencies
RUN apk add --no-cache libffi-dev py-cffi
# https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
RUN apk add --no-cache --update tzdata
# grpcio dependencies
RUN apk add --no-cache g++
# Git dependencies
RUN apk add --no-cache git
# Pip Updated
RUN python -m pip install --upgrade pip
# Pip dependencies
RUN python -m pip install argon2-cffi
# Pip env
RUN pip install pipenv

# Add requirements file
COPY Pipfile Pipfile.lock ./

# Install requirements (save space by not caching)
RUN pipenv install --verbose --system --deploy --dev --clear

# Add  base core
COPY . /app/