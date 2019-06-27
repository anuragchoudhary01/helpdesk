# Helpdesk 

This repository is the flagship Gemini Solutions Product.

The following documentation covers how to setup and run the code.

## Architecture Overview

Helpdesk is designed with a microservice architecture.

## I'm bored - how do I start?

``
git clone <the repo>
cd that_dir
docker-compose up   # ...to run the stack locally
``


## starting all the bits

If you haven't run Helpdesk before, you need to set up a config.yml to point to the DB server.
If you are going to use the DB server started in a docker container then change the DB settings in the config.yml file.


Inside the `api/` directory, run the following:

``
pipenv install
pipenv shell
./start.sh
``

This will setup the required environment and start the backend API server.


