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
  winner integer references players(id),
  loser integer references players(id));

CREATE VIEW wincounter
AS
  SELECT players.id, players.name, COUNT(matches.winner) AS wins
  FROM players
  LEFT JOIN matches ON players.id = matches.winner
  GROUP BY players.id;

CREATE VIEW matchcounter
AS
  SELECT players.id, players.name, 
    COUNT(matches.winner + matches.loser) AS matches
  FROM players
  LEFT JOIN matches ON players.id = matches.winner OR players.id = matches.loser
  GROUP BY players.id;