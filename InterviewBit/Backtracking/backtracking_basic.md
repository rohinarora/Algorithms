Backtracking
Backtracking is trying out all possibilities using recursion, exactly like bruteforce.
Suppose you have to make a series of decisions, among various choices, where :

  * You don’t have enough information to know what to choose
  * Each decision leads to a new set of choices
  * Some sequence of choices (possibly more than one) may be a solution to your problem

Backtracking is a methodical way of trying out various sequences of decisions, until you find one that “works”. Example- Given a maze, find if a path from start to finish exists. At each intersection, you have to decide between three or fewer choices:

    * Go straight
    * Go left
    * Go right

You don’t have enough information to choose correctly. Each choice leads to another set of choices. One or more sequences of choices may (or may not) lead to a solution.
So, you explore each option thoroughly and once you cannot find a solution using the option selected, you come back and try one of the remaining options.


//A pseudocode for the above question would be :

boolean pathFound(Position p) {
  if (p is finish) return true;

  foreach option O from p {
    boolean isThereAPath = pathFound(O);
    if (isThereAPath) return true; // We found a path using option O
  }
  // We have tried all options from this position and none of the options lead to finish.
  // Hence there is no solution possible to finish
  return false;
}
//In general, the usual pseudocode for any backtracking solution is :

boolean solve(Node n) {
  if n is a goal node, return true

  // Or for exploration- when you run out of search space->
  // if (no more choices) return (Node n is goal state)

  foreach option c possible from n {
    try option c
    if solve(c) succeeds, return true
    unmake option c
  }
  return false // tried everything. Nothing found
}


isAnagram-> piggy back on permute



In the end-
https://en.wikipedia.org/wiki/Backtracking

When going for Sudoku -
https://www.youtube.com/watch?v=p-gpaIGRCQI&feature=PlayList&p=FE6E58F856038C69&index=10

N Queen-
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
(Also screenshot on Desktop)
