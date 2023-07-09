# luizalabs-tech-challenge

This project is an API for a fictional Customer/Favorite Product service.

This is a REST service consisting of multiple endpoints for data retrieval and manipulation.

## Choices

This project was built with the following technologies, frameworks and tools: FastAPI as the API framework (including Pydantic for data validation, Sqlalchemy for database manipulation and OpenAPI for generating automatic API documentation), Postgres as the database, Docker (with docker-compose for easier distribution to test reviewers), JWT for access token generation, GitLab CI.

Most of the technology choices were made to prioritize learning new things and solidifying concepts, such as, learning the FastAPI framework (and its underlying libraries) and applying prior Postgres knowledge with Python.

## Requirements

- Python >= 3.6;
- Docker
  - Docker-Compose *optional*
- Postgres


## Running it

We can use the default configuration file, [found here](app/config.py), if wanted, just make sure to create a DB user with those credentials.
If you need some more customization, we'll need a configuration file!
Create a config.json file at the root of the project, like such:

```json
{
    "ADMIN": {
        "username": "SomeUsernameToAuthWith",
        "password": "SomePasswordToAuthWith"
    },
    "SECRET_KEY": "SomeAwesomeSecretKey",
    "DB_URL": "URLWithPortToYourPostgresDB",
    "DB_USER": "UserForYour.luizalabs.DB",
    "DB_PASSWORD": "PasswordForYour.luizalabs.DB",
}
```

### Docker Compose

Docker compose allow us to easily share environments, their setup and so much more. To run this project with docker-compose:

```sh
> cd your/path/to/luizalabs-technical-test/deploy
> docker-compose build && docker-compose up
```

Now you won't need to wory about database configuration and such.

---

### Local instance

This needs the following setup:

- Postgresql service running on the background;
- A Postgresql database called luizalabs.

After clonning the repo you should create a new Python3 virtual environment and activate it. In your terminal, enter the following:

```sh
> cd your/path/to/luizalabs-technical-test
> python -m venv env
> source ./env/bin/activate
```

This will create a new Python3 virtual environment as to not conflict with globally installed packages, and then activate it so that every Python3 and pip3 commands execute on this virtual space.
 
Now, install the required Python packages.

```sh
> pip install -r requirements.txt
```

We're ready to go! Now run it!

```sh
> CONFIG_PATH=<path/to/config.json> uvicorn main:app
```

If in development instead run

```sh
> CONFIG_PATH=<path/to/config.json> unicorn main:app --reload
```

You can now make requests to the API at localhost:8000, have fun!

## Documentation

Basic documentation for the API can be found after running the project and going to either:

- OpenAPI/Swagger => localhost:PORT/docs
- ReDoc => localhost:PORT/redoc

Where PORT is the port the service is running on. Defaults to 8000 when run in a local instance way and to 80 when run through docker-compose.
