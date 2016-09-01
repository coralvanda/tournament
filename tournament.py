#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(db_name="tournament"):
    """Connect to the PostgreSQL database.  

    Returns a database connection and cursor."""
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could not connect to database {}".format(db_name))


def deleteMatches():
    """Remove all the match records from the database."""
    database, cursor = connect()
    cursor.execute("DELETE FROM matches;")
    database.commit()
    database.close()

def deletePlayers():
    """Remove all the player records from the database."""
    database, cursor = connect()
    cursor.execute("DELETE FROM players;")
    database.commit()
    database.close()

def countPlayers():
    """Returns the number of players currently registered."""
    database, cursor = connect()
    cursor.execute("SELECT COUNT(*) FROM players;")
    player_count = cursor.fetchone()[0]
    database.close()
    return player_count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.
  
    Args:
      name: the player's full name (need not be unique).
    """
    database, cursor = connect()
    cursor.execute("""
        INSERT INTO players (name) 
          VALUES (%s);""", (name,))
    database.commit()
    database.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches a player has been in
    """
    database, cursor = connect()
    cursor.execute("""
        SELECT w.id, w.name, w.wins, m.matches
          FROM wincounter AS w
            LEFT JOIN matchcounter AS m
              ON w.id = m.id
        ORDER BY wins DESC""")
    standings = cursor.fetchall() 
    database.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Updates the matches table by adding a match using the two player
    IDs, and updates the winners table by adding the ID from the
    newly created match, as well as the ID of the winner.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    database, cursor = connect()
    cursor.execute("""
        INSERT INTO matches (winner, loser) 
        VALUES (%s, %s);""", (winner, loser))
    database.commit()
    database.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered,
    each player appears exactly once in the pairings.  Each player
    is paired with another player with an equal or nearly-equal 
    win record, that is, a player adjacent to him or her in 
    the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, id2)
        id1: the first player's unique id
        id2: the second player's unique id
    """
    pairings = playerStandings()
    swiss = []
    previous_player = []
    for player in pairings:
        if previous_player:
            swiss.append((previous_player[0], previous_player[1],
                player[0], player[1]))
            previous_player = []
        else:
            previous_player = player
    return swiss