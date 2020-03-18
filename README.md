# luizalabs-technical-test

## API

This project is an API for a fictional Customer/Favorite Product service.

This is a REST service consisting of multiple endpoints for data retrieval and manipulation.

## Requirements

- Python >= 3.6;
- Postgres

## Running it

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
> uvicorn main:app
```

You can now make requests to the API, have fun!