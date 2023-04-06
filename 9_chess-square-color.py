"""Write a getChessSquareColor() function that has parameters column and row. The
function either returns 'black' or 'white' depending on the color at the specified column and
row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the
function returns a blank string."""


# There is a pattern to the colors of a chess board. If the column and row are both even or both
# odd, then the space is white. If one is odd and the other is even, the space is black.
def getChessSquareColor(col, row):
    if col <1 or col > 8 or row < 1 or row > 8:
        return 'Error!'
    if col % 2 == row % 2:
        return 'white'
    else:
        return 'black'
        
print(getChessSquareColor(0,0))