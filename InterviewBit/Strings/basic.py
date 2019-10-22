A = "" #  empty string
A = "Hello" #  string initialized to "Hello"
A[0]
A = A + "Hello" #  O(n) operation and a new copy is created
l = []
l.append('string1')
l.append('string2')
l.append('string3')
print (l) # l is a list of strings
A = ''.join(l) # join the list of strings into single string
print (A)
len(A) # O(1)
