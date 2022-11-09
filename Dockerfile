# Pull base image
FROM python:3.11-slim-bullseye AS code
LABEL maintainer="Kevin Bowen <kevin.bowen@gmail.com>"

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \

# Set python environment variables
ENV DEBUG="${DEBUG}" \
  PYTHONUNBUFFERED=true \
  PYTHONDONTWRITEBYTECODE=true \
  PYTHONFAULTHANDLER=true \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

ENV PATH="/root/.local/bin:$PATH"
COPY poetry.lock pyproject.toml /code/

# Set work directory
WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy project
COPY . /code/

# CMD ["gunicorn", "-c", "config/gunicorn.py", "config.wsgi"]
