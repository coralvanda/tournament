-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

DROP TABLE IF EXISTS players;

CREATE TABLE players (id SERIAL PRIMARY KEY, name TEXT);

DROP TABLE IF EXISTS matches;
 
CREATE TABLE matches (matchID SERIAL PRIMARY KEY,
  p1 integer references players(id),
  p2 integer references players(id));

DROP TABLE IF EXISTS winners;

CREATE TABLE winners (id SERIAL PRIMARY KEY,
  matchID integer references matches(matchID),
  winner integer references players(id));

