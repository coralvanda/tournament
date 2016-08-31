## What is this?
-------------
This is a project created for the Udacity Full-Stack Developer
Nanodegree program.  The tournament.sql file sets up a database
modeling players and matches in a tournement, the tournament.py
file allows for easy interaction with the database in set ways,
and the tournament_test.py file is the instructor-provided code to
test that things were set up and programmed correctly.

## How to use
----------
The user must first run the tournament.sql file to set up the
atabase and tables.  This can be done from the command line.  
From the same directory as the .sql file, first, open the 
PostgreSQL interactive terminal with the command `psql`.  Then run 
the file with `\ir tournament.sql`.  Exit psql by using the 
command `\q`.  Then, also from the command line, use `python 
tournament_test.py` to run the test file.  Test results will be 
printed out to show what aspects of the program passed or failed.  
The tournament.py file does not need to be run directly, but must 
be located in the same directory as the other files.