* The idea of hashing is to distribute the entries (key/value pairs) across an array of buckets
* Hash tables are like arrays. Like arrays, hash tables give constant time lookup
* Arrays vs Hash tables.
  * If data were ordered in continuous integers from 0 to k; we could do constant time lookup, insertion and deletion into the array. But this won't work with any kind of data. this is where hash tables come in
* hash table is like an array "indexed by the [hash of keys] you want to store". array A[i]=A[H[x]] where H is the hash function and x is the key to be stores in hash table.
* Hash tables are really helpful when bulk of the work is simple lookup (into some database). They allow super fast lookup.
* Hash tables are easy to implement badly. Bad hash functions are easy to design (coming up with good hash functions is non trivial)
* Applications
  * De-Duplication
  * 2 Sum

* **Collisions**
  * [Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
      * Excellent article.
      * Actually, a uniform distribution of birth dates is the worst case
  * https://betterexplained.com/articles/understanding-the-birthday-paradox/
  * http://matt.might.net/articles/counting-hash-collisions/

* 2 ways of dealing with hash collisions-open addressing and chaining. Each of them have their own advantages/disadvantages. Implement and see what works best for the problem
  * In general, deletion is difficult with open addressing
  * chaining tends to use more space

* a good hash function "spreads" data evenly across buckets

* 'load' on a hash table

* All hash tables have "pathological data sets" - pigeonhole principle. Hash tables work in hope you don't come across pathological data
* use randomization. guaranteed to do well on average given the assumption that number of objects in hash table is comparable to number of buckets in hash table
* Bloom filters not in CLRS edition 3
