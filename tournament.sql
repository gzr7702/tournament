-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE player (name TEXT,
                     wins INTEGER,
                     matches INTEGER,
                     id SERIAL );

CREATE TABLE match (round INTEGER,
                     player1 TEXT,
                     player2 TEXT,
                     id SERIAL );
