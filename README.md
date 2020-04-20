# EdmondsAlgorithm
### Description:
Repository that contains the implementation of Edmonds' (or Chu–Liu/Edmonds') algorithm. This algorithm solves the following problem: Given a directed graph G where each edge e has a weight w(e), find the minimum cost spanning tree from a root node r.

### Running time: 
O(|V| * |E|) 

### Resources:
Used For: Information on the implementation of Edmonds' algorithm  
URL: https://en.wikipedia.org/wiki/Edmonds%27_algorithm  
Accessed on: April 9th, 2020  
  
Used For: Testing my implementation of Edmonds' algorithm  
URL: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2124  
Accessed on: April 9th, 2020  
  
Used For: Extra test cases to debug my code  
URL: https://www.udebug.com/UVa/11183  
Accessed on: April 13th, 2020  
  
### Instructions For Running Program:
Compile: `make`, `make compile` or `g++ --std=c++11 MDST.cpp -o MDST` 
Run: `time ./MDST < *testfile*`
  
### Pecularities or Assumptions: 
1. In my program I assume that vertex #0 is the root node always.
  
### Summary of Other Files In Project:
Format of test files:  
n m 
u_1 v_1 w_1  
u_2 v_2 w_2  
...  
u_m v_m w_m  
Where n is the number of nodes, m is the number of edges, and each edge is represented by a parent vertex u, child vertex v, and weight w (the edge goes from u -> v)  

- disconnectedGraph.txt: A .txt input file with 10 nodes and 15 edges but is disconnected and thus has no minimum directed spanning tree
- genRandTest.py: A python script that generates a random test file
- genSparseGraph.py: A python script that generates a large sparse graph test file
- genWorstCaseTest.py: A python script that generates a worst case test file (n recursive calls)
- propsal.txt: The proposal I made on eclass
- randTestFile1.txt: A .txt input file with 500 nodes and a random 50000 edges
- randTestFile2.txt: A .txt input file with 1000 nodes and a random 75000 edges
- randTestFile3.txt: A .txt input file with 2000 nodes and a random 100000 edges
- sparseGraph.txt: A .txt input file with 25000 nodes and 24999 edges and is a large connected sparse graph
- worstCase1000.txt: A .txt input file which makes the recursion depth 1000 
- worstCase3000.txt: A .txt input file which makes the recursion depth 3000

For correctness, the test files I used were the ones provided by UVa (linked in resources).
  
### Description of Output:
u_1 1 w_1  
u_2 2 w_2  
...  
u_(n-1) n-1 w_(n-1)
Total sum: *SUM*
  
The program output consists of n - 1 edges that form a minimum directed spanning tree of G as well as a line indicating the total weight of the graph. 
