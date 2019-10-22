-> kth queen is placed at kth row by default. This is implicit in entire code. We output a single array. Assume ith element of this array represents ith row of the grid. And all we need to output is column number corresponding to to ith element of the array.
-> try kth queen on each column from 1 to n
-> place (k,i) -> checks if kth queen can be placed in ith location


place(k,i){   
# can i place kith queen in ith location
# check for collision with k-1 queens

for j=1 to k-1{
if (x[j]==i) or (abs(x[j]-i)==abs(k-j)){
# jth queen in ith column
or
# row difference == coloumn difference gives diagnal position of jth and ith Queens
    return false
}
}
return true
}



nqueen(k,n){
for i = 1 to n # check of queen k can be placed at each column
{
  if place(k,i) # can i place kth queen in ith column?
  {
    x[k]=i
    if k==n{
      print x[]
    }
    else{
      nqueen(k+1,n)
    }
  }
}
}

How to stop? Make nqueen return a boolean true or false->

bool nqueen()

Time complexity- exponential
Space - O(n) (Depth of recursion tree)
