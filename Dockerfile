FROM python:3.9.7

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /mysql-database-connection

COPY *.toml *.lock /mysql-database-connection/


ENV PATH="${PATH}:/root/.poetry/bin"


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .
