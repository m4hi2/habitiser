# Habitiser

A simple habit tracker built with Django. No SPA, no REST, simple plain old
full stack Django.

I'm in new routines and needed a simple way to track my new habits. There are
lots of mobile apps to do this. But most of them are way too cluttered and
wants money to fulfill my need. So, here I'm, making another project that I
*might* not finish.

Oh, if you are yet to get it, this project is very much **WIP**.

Enough babbling... Let's get into work.

## Requirements

Python: 3.13 (because it's latest! You might be able to use lower version, IDK)

Database: Postgresql@14 (because I had it installed.)

## How to run

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Now go ahead, update the `.env` file with your database information.

Let's run the project

```shell
python3 manage.py migrate  # lets run the migrations
python3 manage.py runserver
```

I will later add a **docker compose** to make things simpler.

