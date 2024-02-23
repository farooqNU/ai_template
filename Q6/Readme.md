# Assignment 1 : Question 6
|Std ID|Name|
|------|-|
|i222132|Mursil Hassan|

![image](https://github.com/NUCES-Khi/assign1-7questions-mursil/assets/85949538/fe32debb-209f-4b37-bdc4-fe650bcb2346)

#Explaination
 The code uses functions ,and each function is an algorithm, the goal of the program is to fine the most effective algorithm,
 in order to reach a specific place 
## BFS UCS GBFS IDDFS

 These are the algorithms used within the program, they all work differently.

 **(BFS)** explores neighboring nodes at the current depth before progressing to deeper levels, using a queue to track the next nodes to visit.

 **(UCS)** prioritizes nodes based on their path cost from the source in a weighted graph, maintaining a priority queue.

 **(GBFS)** selects nodes closest to the goal using a heuristic function, employing a priority queue based on heuristic values.

 **(IDDFS)** combines BFS and DFS, gradually increasing the depth limit until finding the target node.







## MAIN
 The main part of the code takes input for the source and destination nodes, checks if they exist in the graph, and then runs each of the
 search algorithms. After finding paths, it computes their costs and prints the results, including the shortest path algorithms in ascending 
 order of their costs.


 ## Result 

 The Screen shot shows that that BFS had the least cost as compared to all other algos used.





 
