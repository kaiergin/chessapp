Chess Game Final Project:
Consists of a generated chess board with coordinate layout using tkinter
Each side will have a class with sub classes for pieces
Calculations will have to be made for each class’s possible movement
Bot will think up to 4 moves ahead looking at every move possibility and taking the path that results in the most possible points (based on piece captures)

----------------
NOTE: 
Because of complications when working with tkinter, the following were not able to work
- creating transparent buttons ontop of labels
- creating transparent labels ontop of buttons
- saving multiple different buttons to a list
There were work arounds but much extra code was needed
----------------

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
