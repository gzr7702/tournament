-- Table definitions for the tournament project. 
--
--


CREATE TABLE player (
                    id SERIAL primary key,
					name VARCHAR(75)
					);

CREATE TABLE match (
                    id SERIAL primary key,
					round INTEGER,
                    winner INTEGER REFERENCES player (id),
                    loser INTEGER REFERENCES player (id)
                    );
