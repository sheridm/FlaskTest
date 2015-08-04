#!flask/bin/python
"""
Before running remember to physically create database using postgres!
Make sure to close all connections / python scripts looking at database otherwise errors occur.
RUN this script from the cmd line.

to create a migrations folder -
# python c:\python27\donalworkarea\webdev\gscore_v0\db_create_migrate.py db init
(it will say Please edit ... before proceding; this is not an error, just info.)

run these two (each will flash INFO messages) for every model change (including the first model-overlay on blank dbase) -
# python c:\python27\donalworkarea\webdev\gscore_v0\db_create_migrate.py db migrate
[migrate generates one empty table: alembic_version]

# python c:\python27\donalworkarea\webdev\gscore_v0\db_create_migrate.py db upgrade
[generates all the other tables]

then follow up with - 
python c:/... gscore_v0/db_init_data.py 
[to populate]
or python db_init_data.py init_data (from shell)

# we can of course also run: python c:\... db downgrade
"""
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()