# Willard, Daniel helped with pseudocode/algorithm
# had dfs originally but couldn't get it to work
# worked with Ash as well

import sys
from sys import stdin
from collections import defaultdict

def bellman_ford(n, m, g):
    distance = [float("-inf")]*(n+1)
    count = [1]*(n+1)
    distance[1] = 0

    # bellman ford algorithm
    for node in range(n):
        for j,w in g[node]:
            # relax edges
            if distance[j] < distance[node] + w:
                distance[j] = distance[node] + w
                count[j] = count[node]
            elif distance[j] == distance[node] + w:
                count[j] += count[node]
    longest_path = distance[n]
    number_of_longest_paths = count[n]
    return longest_path, number_of_longest_paths



'''
for each node
   for each turple in my adj_list
    if v.dist < u.dist + w
      update
      v.count =u.count
    elif v.dist == u.dist +w
      v.count += u.count


def dfs(G, vertix, edge_seen = None, path = None):
    if edge_seen is None: edge_seen = []
    if path is None: path = [vertix]

    edge_seen.append(vertix)

    paths = []
    for t in G[vertix]:
        if t not in edge_seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(dfs(G, t, edge_seen[:], t_path))
    return paths


def longest_path():
    

def num_of_longest_path():
'''


# G = defaultdict(list)
# edges = sys.stdin.read().strip()
# input_str = read_input_file(edges)
# x, y, z = parse_input(input_str)



#all_paths = dfs(G, '1')
#max_len   = max(len(p) for p in all_paths)
#max_paths = [p for p in all_paths if len(p) == max_len]


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    # print("n", n)
    # print("m", m)
    g = defaultdict(list)
    for p in range(m):
        i,j,w = map(int, sys.stdin.readline().split())
        g[i].append((j, w))
    # print("g", g)


longest_path, number_of_longest_paths = bellman_ford(n, m, g)
print("Longest path: ", longest_path)
print("Number of longest paths: ", number_of_longest_paths)

