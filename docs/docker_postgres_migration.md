### Django database migration from sqlite3 to Docker postgres

---

If there is an existing Docker container for the app, install the postgres
database adapter now.(This assumes that the `environs` package is already
installed, configured and being used.)

    a. `docker-compose up`
    b. `docker-compose exec web poetry add psycopg2-binary`
    c. `docker-compose down`

1. Comment out the environment variable `DATABASE_URL` in the file `.env`,
    Otherwise any existing local sqlite3 db file will be overwritten and
    existing data will be lost.

2. Add the following to `docker-compose.yml`:
```
services:
  web:
    ...
    depends_on:
      - db
    environment:
      - "DEBUG=True"
  db:
    image: postgres:11
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"

volumes:
  postgres_data:
```
3. Build new Docker image
    `docker-compose up --build`
4. Install postgres db adapter (For new installations only)
    `docker-compose exec web poetry install psycopg2-binary`
  a. `docker-compose down`
  b. `docker-compose up --build`
5. Apply database migrations
    `docker-compose exec web python manage.py migrate`
4. Create superuser
    `docker-compose exec web python manage.py createsuperuser`

NOTES:
Log message generated on initial build:
```
Attaching to message_board_db_1, message_board_web_1
db_1   | ********************************************************************************
db_1   | WARNING: POSTGRES_HOST_AUTH_METHOD has been set to "trust". This will allow
db_1   |          anyone with access to the Postgres port to access your database without
db_1   |          a password, even if POSTGRES_PASSWORD is set. See PostgreSQL
db_1   |          documentation about "trust":
db_1   |          https://www.postgresql.org/docs/current/auth-trust.html
db_1   |          In Docker's default configuration, this is effectively any other
db_1   |          container on the same system.
db_1   |
db_1   |          It is not recommended to use POSTGRES_HOST_AUTH_METHOD=trust. Replace
db_1   |          it with "-e POSTGRES_PASSWORD=password" instead to set a password in
db_1   |          "docker run".
db_1   | ********************************************************************************
db_1   | The files belonging to this database system will be owned by user "postgres".
db_1   | This user must also own the server process.
db_1   |
db_1   | The database cluster will be initialized with locale "en_US.utf8".
db_1   | The default database encoding has accordingly been set to "UTF8".
db_1   | The default text search configuration will be set to "english".
db_1   |
db_1   | Data page checksums are disabled.
...snip...
db_1   | WARNING: enabling "trust" authentication for local connections
db_1   | You can change this by editing pg_hba.conf or using the option -A, or
db_1   | --auth-local and --auth-host, the next time you run initdb.
db_1   |
db_1   | Success. You can now start the database server using:
db_1   |
db_1   |     pg_ctl -D /var/lib/postgresql/data -l logfile start
```
