
# coding: utf-8

# # EX-1 & EX-2

# Essays Reviews submitted

# # EX-3: Three-Hop Edges

# In[161]:


from IPython.display import Image

Image(filename='3Hoop.png')


# In[163]:


import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Adjacency:
    
    def __init__(self,matrix):
        self.curr_matrix=matrix
    
    def Three_hop(self,matrix):
        hop_matrix = matrix*matrix*matrix
        return self.into_1s(hop_matrix)
        
    
    def into_1s(self,matrix):
        test = matrix.tolist()
        for i in range(len(test)):
            for j in range(len(test[i])):
                if(test[i][j]>1):
                    test[i][j]=1
        matrix=np.array(test)
        return matrix
    
    def Transitive_Closure(self,matrix):
        G = self.into_1s(matrix*matrix)
#         G=matrix*matrix
        print('\n------G1------\n')
        print(G)
        G2 = self.into_1s(G*G)
#         G2 = G*G
        print('\n------G2------\n')
        print(G2)
        G4 = self.into_1s(G2*G2)
#         G4 = G2*G2
        print('\n------G4------\n')
        print(G4)
        G8 = self.into_1s(G4*G4)
#         G8 = G4*G4
        print('\n------G8------\n')
        print(G8)
        
        
    
    def warshall(self,a):
        assert (len(row) == len(a) for row in a)
        n = len(a)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    a[i][j] = a[i][j] or (a[i][k] and a[k][j])
        return a
        


# In[164]:


adj_matrix = Adjacency(np.matrix([[0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,1,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0]]))

print('Adjacenct matrix of Directed Graph\n')
print(adj_matrix.curr_matrix)

print('\n**********************************')
print('\n3-Hop Edged Adjaceny Matrix\n')

print(adj_matrix.Three_hop(adj_matrix.curr_matrix))


# ### 3 Hop Steps
# 
# Reachable paths in 3 steps are following. <br>
# 
# 1: A -> H,K <br>
# 2: B -> NULL<br>
# 3: C -> E,F,H,K<br>
# 4: D -> E, H, J, K<br>
# 5: E -> E, H, K<br>
# 6: F -> E, F<br>
# 7: G -> E, F<br>
# 8: H -> H, K<br>
# 9: I -> H, K<br>
# 10:J -> E<br>
# 11:K -> E, F<br>
# 

# In[39]:


Image(filename='3HoopEdgeGraph.png')


# ### Description:
# 
# The adjacency matrix for a graph with n vertices is an n × n matrix whose (i,j) entry is 1 if the ith vertex and jth 
# vertex are connected, and  0 if they are not. In the above directed graph, for all the vetices from A to K the adjacency matrix is calculated and shown in the above graph.

# # EX-4: Transitive Closure & Warshal's Algorithm
# 
# ## Code Reference for Warshal's in Adjacency Class implemented above:
# https://stackoverflow.com/questions/22519680/warshalls-algorithm-for-transitive-closurepython

# ## 1- Transitive Closure

# In[84]:


adj_matrix2 = Adjacency(np.matrix([[1,1,0,0,0,1,0,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0,0],
               [0,1,1,0,1,0,1,0,0,0,0],
               [0,0,1,1,0,0,0,0,0,0,0],
               [0,0,0,0,1,0,0,1,0,0,1],
               [0,0,0,0,1,1,0,0,0,0,0],
               [0,0,0,0,1,0,1,0,0,1,0],
               [0,0,0,0,0,1,0,1,0,0,0],
               [0,0,0,0,0,0,1,0,1,0,0],
               [0,0,0,0,0,0,0,1,0,1,0],
               [0,0,0,0,1,0,0,0,0,0,1]]))

adj_matrix2.Transitive_Closure(adj_matrix2.curr_matrix)


# #### Description:
# 
# Given a digraph G, the transitive closure is a digraph G' such that(i,j) is an edge in G' if there is directed path from i to j in G. The resultant digraph G' representation in form of adjacency matrix is called the connectivity matrix <br>

# ## 2- Floyd Warshall Algorithm

# In[89]:


print(np.array(adj_matrix2.warshall((adj_matrix2.curr_matrix).tolist())))


# #### Description:
# #### Defintion source:Wikipedia
# 
# "This algorithm is used to find theshortest path in a weighted graph. The edges of the graph can have positive and negetive weights but not with negetive cycle" 
# 
# #### Comparision
# Here the transitive closure we calculated previously gives us the same matrix as of the matrix returned by Floyed Warshal's algorithm. 
# 

# # EX-5 Random Walk Algorithm
# 
# 

# #### Creating DiGraph of given graph from Networkx Library

# In[98]:


graph = nx.DiGraph()
graph.add_edges_from([(0, 1), (0, 5), (2, 1), (2, 4), (2, 6), (3, 2), (4, 7), (4, 10),
                  (5, 4), (6, 4), (6, 9), (7, 5), (8, 6), (9, 8), (10, 4)])

graph_adjaceny_list = defaultdict(list)
for (i, j) in graph.edges():
    graph_adjaceny_list[i].append(j)


# ### Subtask-1: Random Re-appearing
# 
# ### Subtask-2: Probabilistic Random Re-appearing

# In[182]:



def Random_Reappear(dic, initial, path=[], last=random.choice(list(G_dict))):
    path.append(initial)

    if initial == last or len(path) >= 500:
        return path
    elif initial not in dic.keys():
        up_node = random.choice(list(G_dict))
    else:
        if len(dic[initial]) != 0:
            up_node = dic[initial][random.randint(0, len(dic[initial]) - 1)]
        else:
            up_node = random.choice(list(G_dict))
            while up_node == initial:
                up_node = random.choice(list(G_dict))

    Random_Reappear(G_dict, up_node)
    return path


#print("\n\n------------------------------------------------------------------------------------\n\n")


def probabilistic_Random(dic, initial, path=[], last=random.choice(list(G_dict))):
    path.append(initial)

    if initial == last or len(path) >= 900:
        return path
    elif initial not in dic.keys():
        up_node = random.choice(list(G_dict))
    else:
        pval = random.randint(1, 10)
        if len(dic[initial]) != 0 and pval > 2:
            up_node = dic[initial][random.randint(0, len(dic[initial]) - 1)]
        elif len(dic[initial]) != 0 and pval < 3:
            up_node = random.choice(list(G_dict))
            while up_node == initial:
                up_node = random.choice(list(G_dict))
        else:
            up_node = random.choice(list(G_dict))
            while up_node == initial:
                up_node = random.choice(list(G_dict))

    probabilistic_Random(G_dict, up_node)
    return path


myinitial = random.choice(list(graph_adjaceny_list))

random_walk = Random_Reappear(graph_adjaceny_list,myinitial)
probabilistic_walk = probabilistic_Random(graph_adjaceny_list, myinitial)
# for elem in random_walk:
#     print(elem)
print("Random Walk:\n")
print(random_walk,"\n")
print("\n------------------------------------------------------------------------------------\n")
# for elem in probabilistic_walk:
#     print(elem)
print("Probabilistic Walk:\n")
print(probabilistic_walk)


# ### Frequency of Most Visited Node in Random Walk and Probabilistic Walk:

# In[190]:


plt.hist(random_walk,color="purple")
plt.xlabel('Vertices')
plt.ylabel('Frequency')
plt.show()


# In[191]:


plt.hist(probabilistic_walk, color="red")
plt.xlabel('Vertices')
plt.ylabel('Frequency')
plt.show()


# ### Description:
# 
# The random walk algorithm is an algorithm in which we randomly visit graph's nodes. The algorithm has many applications. For example in social networks we can do link prediction by randomly waling on the network graph in which people are nodes.
# 
# In above implemented random walk algorithm we applied two approaches. The first approach was the naive approach in which in case of dead end we just randomly choose another node from and the graph and start walking from that node.
# In the second approach we gave 2 probabilites of choosing a node. We assigned 80% probability to the neighbouring nodes of the current nodes and 20% to randomly choose nodes.
# The above histograms shows the most visited nodes frequency and we can infer from the above histograms that the 4th node was the most important node in both of our implementations because its frequency is highest compared to all other nodes.
