-- Table definitions for the tournament project. 
--
--


CREATE TABLE player (name TEXT,
                     wins INTEGER,
                     matches INTEGER,
                     id SERIAL );

CREATE TABLE match (round INTEGER,
                     player1 TEXT,
                     player2 TEXT,
                     id SERIAL );
