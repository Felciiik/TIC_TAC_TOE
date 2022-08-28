# TIC TAC TOE game 

## Basic version

<ul>
<li> Create a board using a 2-dimensional array and initialize each element as empty.</li>
    <ul>
        <li> You can represent empty using any symbol you like. Here, we are going to use a hyphen. '-'. </li>
    </ul> 
<li> Write a function to check whether the board is filled or not. </li>
    <ul>
        <li> Iterate over the board and return false if the board contains an empty sign or else return true. </li>
    </ul>
        
<li> Write a function to check whether a player has won or not. </li> 
    <ul>
        <li> We have to check all the possibilities that we discussed in the previous section.</li>
         <li> Check for all the rows, columns, and two diagonals. </li>
    </ul>
<li> Write a function to show the board as we will show the board multiple times to the users while they are playing. </li> 
<li> Write a function to start the game. </li> 
    <ul>
        <li> Select the first turn of the player randomly.</li>
        <li> Write an infinite loop that breaks when the game is over (either win or draw).</li>
            <ul>
                <li> Show the board to the user to select the spot for the next move.</li>
                <li> Ask the user to enter the row and column number. </li>
                <li> Update the spot with the respective player sign.</li>
                <li> Check whether the current player won the game or not.</li>
                <li> If the current player won the game, then print a winning message and break the infinite loop.</li>
                <li> Next, check whether the board is filled or not.</li>
                <li> If the board is filled, then print the draw message and break the infinite loop.</li>
            </ul>
        <li> Finally, show the user the final view of the board.</li>
    </ul> 
</ul>

## AI version
<ul> 
<li> Future idea. - To be specified and implemented in the future.</li>
</ul>

## Generalized version
<ul> 
<li> Future idea. - To be specified and implemented in the future. (Tut: https://www.youtube.com/watch?v=Ff9zSoV5Xgo) </li>
</ul>
