Chess Game Final Project:
Consists of a generated chess board with coordinate layout using tkinter
Each side will have a class with sub classes for pieces
Calculations will have to be made for each class’s possible movement
Bot will think up to 4 moves ahead looking at every move possibility and taking the path that results in the most possible points (based on piece captures)

This technically is my first REAL coding project

----------------
NOTE: 
Because of complications when working with tkinter, the following were not able to work
- creating transparent buttons ontop of labels
- creating transparent labels ontop of buttons
- saving multiple different buttons to a list
There were work arounds but much extra code was needed
----------------

Acknoledgements:
I realize that the program could have been much shorter if I used dictionaries for pieces/images. I also realize that if pieces used inheritance that the code would have been simpler and more efficient.
I now also realize that if I made temporary saves of the board before every move was made, it would be much simpler to revert back to the previous game state when an illegal move is made.
Because I started this project halfway through my python class, I had not learned about these things and by the time I learned them, it would have been more work to go back and change them.
I also have found out that my coding etiquette is very bad. Some of my lines are way to long and I use a lot of improper spacing. Sorry.

Update: Chess game movement complete. Pieces still don’t have chess logic and do not understand player turns. Hopefully will add in turns and some of chess logic before end of class.

Update 1/13/2016: Turns added

Update 1/15/2016: Chess logic started. Basic frame added. Working for pawns but does not recognize when a piece jumps over another piece. Will fix soon.

Update 1/19/2016: Pawn logic finished. Rook logic in progress.

Update 1/20/2016: Rook logic finished. Knight logic finished. Bishop logic in progress.

Update 1/21/2016: Bishop logic finished. Queen logic finished. Added support for python 2.7. Resized images to half size.

To do: Add king logic. Add castling. Add pawn to queen change. Add check (Maybe checkmate). Add separate side frame. Add undo button. Add redo game button. Add list of captured pieces. Add option to change piece size upon launch.

Update 1/21/2016: King logic finished (not check or checkmate). Side frame added. Redo game button added.

Update 1/22/2016: Changed piece movement to highlight piece when selected. Started to add pawn to queen when pawn reaches opposite side of board. Code comments coming soon.

Update 1/22/2016: Pawn changes to queen when other side is reached.

Update 1/25/2016: King bug fixed. Check logic started. Code comments started. Made function for switching resetting turn if false move is made. Saved about 250 lines of code.

Update 5/10/2016: Check completed. Debugging in progress. Code comments will be added next. En Passant, Castling, and Checkmate are planned.

Update 5/11/2016: A few Check bug fixes. Also a black bishop bug fix where it would turn into a white bishop.

Update 5/16/2016: Code comments in ChessGameClasses added.

Update 5/18/2016: Checkmate added. Stalemate planned. Bugs are still possible in Checkmate. An undo feature is being planned, allowing players to take back as many turns as they want. This will be done by saving previous board configurations to a text file.

Update 5/19/2016: Stalemate added. Castling added. Possible bugs when moving pawn -> queen but in check. Testing will be necessary.

Update 5/23/2016: En Passant added. Possible bugs when checking for checkmate after castling or after En Passant. AI is planned.

Update 5/24/2016: Initial bot created. At the moment can only think in the present move. Bot not tested or added into the script.
