#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM match;')
        db.commit()
        db.close()
    except psycopg2.Error as e:
        print(e)

def deletePlayers():
    """Remove all the player records from the database."""
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute('DELETE FROM player;')
        db.commit()
        db.close()
    except psycopg2.Error as e:
        print(e)


def countPlayers():
    """Returns the number of players currently registered."""
    count = None
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute('SELECT count(*) FROM player;')
        count = cursor.fetchone()[0]
        db.close()
    except psycopg2.Error as e:
        print(e)

    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO player (name, wins, matches) VALUES (%s, %s, %s);" , (name, 0, 0))
        db.commit()
        db.close()
    except psycopg2.Error as e:
        print(e)



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    standings = []
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute(' SELECT (id, name, wins, matches) FROM player order by(matches);')
        results = cursor.fetchall()
        db.close()
    except psycopg2.Error as e:
        print(e)

    for result in results:
        stripped_record = result[0].lstrip('(').rstrip(')')
        record_list = stripped_record.split(',')
        record_list[1] = record_list[1].strip('\"')
        record_list[2] = int(record_list[2])
        record_list[3] = int(record_list[3])
        record = tuple(record_list)
        standings.append(record)

    return standings 


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute("UPDATE player SET wins = wins+1, matches = matches+1 WHERE id=%s;" % winner)
        cursor.execute("UPDATE player SET matches = matches+1 WHERE id=%s;" % loser)
        db.commit()
        db.close()
    except psycopg2.Error as e:
        print(e)
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


