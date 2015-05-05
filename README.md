This is the implementation of a Swiss Tournament System. A Swiss Tournament is
one in which all players play in each round. In each round, the players are matched
by the number of wins they have.

Inatallation:

This application uses Python 2.7 and PostgreSQL 9.3.6

You must also intsall the psycopg2 library. This is easily done by using pip:

pip install psycopg2

Once you have that, you need to create the database. Connect to the psql command prompt (psql)
and type:

CREATE DATABASE tournament;

Then connect to the database:

\c tournament

and run the command to create the schema:

\i tournament.sql

Now that you have the datbase prepared, you can run the tests to make sure
everything is working:

python tournament_test.py

This should tell you that all tests have passed and you are ready to use the library.

Files:

tournament.py - the main module
tournament_test.py - the test module
tournament.sql - the database schema