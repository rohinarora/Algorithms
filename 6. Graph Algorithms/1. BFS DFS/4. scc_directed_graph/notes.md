* non obvious to find SCC of DG (directed graphs) (was more obvious to find CC of undirected graph (UG); when we used BFS)
* CC vs SCC
  * a and b SCC means can go from a->b and b->a. will happen in the "cyclic" parts of DG
  * a and b are CC and not SCC if we can go from a->b only
    * happens in "acylic parts" of directed graphs
  * CC and SCC have same meaning for UG. For UG, prefer to use the word CC.
  * CC of UG-> BFS or DFS
* SCC takes input an entire graph (and no specific starting node.). The starting nodes are found by Kosaraju's algorithm
* ToDo
  * 3. structure_of_the_web.pdf
