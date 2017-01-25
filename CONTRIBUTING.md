# Contributing to the project

**IMPORTANT**: This document is meant for a development environment. Although
it does contain basic information that will be useful for both testing and
production environments, a production environment will most likely need
specific configurations to function properly. An experienced professional
should be consulted.


## Install and update

In order to run this software, you will need a proper environment. Follow the
steps below to get a working environment.

1. Make sure your system fulfills the following list of basic software. Be sure
   to workaround any eventual naming differences according to the operating
   system maintainer.

   - Python 3.6 (often `python`)
   - Python virtualenvwrapper (often `python-virtualenvwrapper`)
   - PostgreSQL 9.6 (often `postgresql`)
   - PostgreSQL development headers (often `libpq-dev`)

1. Create a [virtualenv]() with Python 3.6.x:

    ```sh
    $ mkvirtualenv -p $(which python3) my-project
    ```

    The `mkvirtualenv` command will already activate the newly created
    environment. In order to activate it in a later time, be sure to run:

    ```sh
    $ workon my-project
    ```

1. Set up a PostgreSQL database to store data. Make sure to have proper
   administrator access in order to create and configure the new database.

    ```sh
    $ createdb my-project
    ```

    Although you can also use another database system, we recommend that a new
    environment replicates a production environment as much as possible.

1. Create a file named `.env` and change any necessary environment-specific
   configuration. Refer to the included `example.env` to learn more about each
   option.

   ```sh
   $ cp example.env .env
   # Edit .env to match your environment
   ```

1. Use the built-in script to configure and install required third-party
   software and run any necessary database migrations.

   ```sh
   $ make dev-setup
   ```

   Remember to re-run this command every time the source code gets updated.
   This will make sure that the environment is ready to run the newest version
   of this project.


## Running

Having an environment prepared, according to the steps above, running the
software is easy:

```sh
$ ./manage.py runserver
```

This command will start a **development server** and display the URL to access
it using a browser. Note that this is intended for a local development
environment only! To run this software in a production environment, an
experienced developer should be consulted.


## Test

Execute the command below to run all the unit test suites and compile a code
coverage report:

```sh
$ make test
```


## Conventions

*TODO: Add contribution rules as we evolve.*


[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
