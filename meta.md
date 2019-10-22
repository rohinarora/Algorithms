* Python always gives positive remainder. C++ can give negative remainder.

https://stackoverflow.com/questions/1907565/c-and-python-different-behaviour-of-the-modulo-operation

2 things can be done with c++ ->
    -   Always use ((n % M) + M) % M in place of (n % M) with C++ -> best method
    -   Or upon computation-
        out=n%M
        if out < 0: return out+M
        else : return out
* Prefer to use "long long" datatypes when big numbers come up in C++. Just using "int" might give wrong answer and you might not even realize  



* Questions-
How is Interviewbit/Backtracking/Subsets/sol3.py working? Generators. Not clear
Python3 lightweight solution-
https://www.interviewbit.com/problems/subset/


* Understand "problem" patterns. Example- All backtracking problems fit into a single frame. (Apart from problem related tricks). But have a solid understanding of problem patterns, and a generalized framework to attack each problem type


*
Java-
