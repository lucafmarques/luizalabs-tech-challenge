# luizalabs-technical-test

This project is an API for a fictional Customer/Favorite Product service.

This is a REST service consisting of multiple endpoints for data retrieval and manipulation.

---

## Requirements

- Python >= 3.6;
- Docker
  - Docker-Compose (if wanted)
- Postgres

---

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
> cd your/path/to/luizalabs-technical-test
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
> CONFIG_PATH=<path/to/config.json> uvicorn --port 80 main:app
```

If in development instead run

```sh
> CONFIG_PATH=<path/to/config.json> unicorn --port 80 main:app --reload
```

You can now make requests to the API, have fun!

---

## Documentation

Basic documentation for the API can be found after running the project and going to either:

- [OpenAPI/Swagger](http://localhost:80/docs)
- [ReDoc](http://localhost:80/redoc)