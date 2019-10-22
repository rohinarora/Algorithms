signed and unsigned representation (in signed MSB represents the sign)

right shift by x bits => division by pow(2, x)
left shift by x bits => mult by pow(2, x)


Tricks
 x & (x-1) will clear the lowest set bit of x
 x & ~(x-1) extracts the lowest set bit of x (all others are clear). Pretty patterns when applied linear sequence.
 x & (x + (1 << n)) = x, with the run of set bits (possibly length 0) starting at bit n cleared.
 x & ~(x + (1 << n)) = the run of set bits (possibly length 0) in x, starting at bit n.
 x | (x + 1) = x with the lowest cleared bit set.
 x | ~(x + 1) = extracts the lowest cleared bit of x (all others are set).
 x | (x - (1 << n)) = x, with the run of cleared bits (possibly length 0) starting at bit n set.
 x | ~(x - (1 << n)) = the lowest run of cleared bits (possibly length 0) in x, starting at bit n are  only clear bits.


Bitwise and Logical Operators
 & is very different from &&. Similarly | is very different from ||
 & or | work on integers performing the operator on each corresponding bits. However, && or || work on boolean values ( Any non zero value is true ) to produce a boolean result.
 2  |   1  = 3
 2  ||  1  = true
 2   &  1  =  0
 2  &&  1  = true

Not done:
boolean arithmetic with signed numbers
