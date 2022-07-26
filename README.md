# trello_cli Introduction
This is a simple Trello command line interface I developed for a challenge.
Cards are inserted and deleted directly (using requests) into a Trello public board, in a dummy account I set up beforehand. (https://trello.com/b/vzsjBgwW/test-board)

I used sqlite as a backup database that should be a mirror of the Cards that are currently on the Board.
The task was to allow insertion only on 'Problems', 'Working' and 'Ready' Lists. Therefore those Lists are kind of hardcoded(on the menu, not by id). However with a few edits it could be used with whatever Lists you need.
I wanted to implement a few other options and include some tests but I was kinda tight with time in my schedule this week.

## More in Depth
trello_cli.py is the main program and Trello.py is the class I made to encapsulate all the requests. 
This last one can be expanded if more functionality is needed. At first I prototyped a Boards-Lists-Cards Class model but then discarded it.
the first part of the menu is kinda self explanatory, you first need to select the list to operate, then the task you want to do with that list.
the database only has the Cards table, I wanted to add the entire main database structure(I mean Boards-Lists-Cards) used on Trello but I as I mentioned above I was short on time.

'Display cards' will show all the cards on the current list. this is requested only from the online Trello Board, since the db was added later.

'Add new card' will add a new card into the current list, both on the database and in the online Trello Board.

'Delete cards' will delete all cards on current list, both on the database and in the online Trello Board. I added this for testing to clean the list and start from scratch.

To check if Cards are actually on both the Trello Online Board and in sqlite database you can use this https://sqlitebrowser.org/, I used the portable version.
Actually, I got distracted and started programming a simple sqlite cmd because I didn't wanted to use an external tool. But then I remembered that the clock was ticking.

## Libraries used
I believe sqlite3 is included on Python 3 by default, otherwise:
```
pip install pysqlite3 
```
I've also used Requests:
```
pip install requests
```
