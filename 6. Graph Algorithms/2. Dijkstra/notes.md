dijk becomes BFS is all the edge weights are equal/1

at each iteration we compute shortest distance to 1 new vertex. each iterations grows the set X by 1
only consider edges with tail in {X} and head in {V-X}






Dijkstra's shortest-path algorithm- works in any directed graph with non-negative edge lengths, and it computes the shortest paths from a source vertex to all other vertices. Particularly nice is the blazingly fast implementation that uses a heap data structure (more on heaps next week).

THE HOMEWORK: Problem Set #2 should solidify your understanding of Dijkstra's shortest-path algorithm. In the programming assignment you'll implement Dijkstra's algorithm. You can just implement the basic version, but those of you who want a bigger challenge are encouraged to devise a heap-based implementation.
