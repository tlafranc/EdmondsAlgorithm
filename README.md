# EdmondsAlgorithm
Description:
Repository that contains the implementation of Edmonds' (or Chu–Liu/Edmonds') algorithm. This algorithm solves the following problem: Given a directed graph G where each edge e has a weight w(e), find the minimum cost spanning tree from a root node r.

Running time: 
O(|V| * |E|) 

Resources:
Used For: Information on the implementation of Edmonds' algorithm
URL: https://en.wikipedia.org/wiki/Edmonds%27_algorithm
Accessed on: April 9th, 2020

Used For: Testing my implementation of Edmonds' algorithm
URL: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2124
Accessed on: April 9th, 2020

Used For: Extra test cases to debug my code
URL: https://www.udebug.com/UVa/11183
Accessed on: April 13th, 2020
    
Instructions For Running Program:
Compile: g++ --std=c++11 MDST.cpp -o MDST
Run: time ./MDST < *testfile*


Pecularities or Assumptions: 
1. In my program I assume that vertex #0 is the root node always.

Summary of Other Files In Project:
- genRandTest.py: A python script that generates a random test file of proper format
- genWorstCaseTest.py: A python script that generates a worst case test file (n recursive calls)

Description of Output:

