import datetime
import random
import sqlite3

import click 
from flask import current_app, g
from flask.cli import with_appcontext

from faker import Faker

def get_db():
    if 'db' not in g: 
        dbname = current_app.config['DATABASE'] 
        g.db = sqlite3.connect(dbname)
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # Create the tables
    f = current_app.open_resource("sql/000_initial.sql")
    sql_code = f.read().decode("ascii")
    cur = db.cursor()
    cur.executescript(sql_code)
    cur.close()
    db.commit()

    faker = Faker() # Used to create dummy data
    cur = db.cursor()
    # Add dummy data
    tags = ["first owner", "family", "trained", "vaccinated", "stray", "adopter", "premium", "bred", "store pick", "well behaved", "exceptional", "contest"]
    for i in tags:
        cur.execute("INSERT INTO tag (name) VALUES (?)", [i])
    click.echo("Tags added")

    for id_, i in enumerate(["cat", "dog", "parrot"], start=1):
        cur.execute("INSERT INTO animal (id, name) VALUES (?, ?)", [id_, i])
        for _ in range(1, random.randint(8,20)):
            name = faker.last_name()
            bought = datetime.datetime.strptime(faker.date(), '%Y-%m-%d').date()
            if random.randint(0,1) == 1:
                sold = bought + datetime.timedelta(days=random.randint(5, 30))
            else:
                sold = ''
            description = faker.text(max_nb_chars = 1000)
            cur.execute("INSERT INTO pet (name, bought, sold, description, species) VALUES (?, ?, ?, ?, ?)", [name, bought, sold, description, id_])
            db.commit()
            cur.execute("SELECT id from pet ORDER BY ID DESC LIMIT 1");
            pet_id = cur.fetchone()[0]
            selected = set(random.choice(tags) for _ in range(random.randint(1, len(tags)//2)))
            for tag in selected:
                cur.execute("INSERT INTO tags_pets (pet, tag) VALUES (?, (SELECT id FROM tag WHERE name=?))", [pet_id, tag])

    click.echo("Species and pets added")
    cur.close()
    db.commit()
    close_db()

@click.command('initdb', help="initialise the database")
@with_appcontext
def init_db_command():
    init_db()
    click.echo('DB initialised') 

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

