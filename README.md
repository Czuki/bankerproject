# bankerproject

bank-accounts management app

#### Implemented:
- basic templates 
- easy-start bash scripts `./run`
- starting with docker-compose
- user login and registration
- bank-account creation - using admin panel or with API

#### TODO:

- PostgreSQL database
- account operations - deposit/withdraw and transfer to another account - with API and user panel
- tests, including testing with selenium
- ...

### First start:

`git clone git@github.com:Czuki/bankerproject.git`

add project directory as `PROJECT_ROOT` in `env.sh` file

`./run env_init` to create virtualenv and install requirements

`./run manage migrate`

`./run start` - app will start at http://127.0.0.1:8000/

### To start with docker-compose

`git clone git@github.com:Czuki/bankerproject.git`

`docker-compose up -d` - app will start at http://0.0.0.0:8000/
