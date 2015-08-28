-- Table definitions for the tournament project. 
--
--

DROP DATABASE tournament;
DROP VIEW wins;
DROP TABLE player CASCADE;
DROP TABLE match;
CREATE DATABASE tournament;

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

CREATE VIEW match_count AS SELECT COUNT(*)
			FROM match
			GROUP BY winner, loser; 