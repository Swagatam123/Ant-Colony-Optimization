'''
Created on Nov 9, 2018

@author: swagatam
'''
import matplotlib.pyplot as plt
import numpy as np

def total_allowed_distance(current_city, moves):
    total = 0;
    for mv in moves:
        total = total + ((pheromone_matrix[current_city][mv]) ** 0.7) * (
                    (inverse_distance_matrix[current_city][mv]) ** 0.7)
    # print("total prob",total)
    return total


def calculate_probability(current_city, adj, total):
    return ((pheromone_matrix[current_city][adj] ** 0.7) * (inverse_distance_matrix[current_city][adj] ** 0.7)) / total;


def update_pheromone(ant_dict):
    #current_pheromone = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    current_pheromone = []
    for i in range(city):
        l =[]
        for j in range(city):
            l.append(0);
        current_pheromone.append(l)
    max1 = -1
    for ant in ant_dict:
        visited = ant_dict[ant]["visited"]
        if(ant_dict[ant]["distance"]>max1):
            max1 = ant_dict[ant]["distance"]
        if len(visited) == city + 1:
            # print(visited)
            for v in range(1, len(visited)):
                # print(visited[v-1])
                # print(visited[v])
                # for i in range(city):
                #    for j in range(city):
                #        if (i==visited[v] and j==visited[v-1]) or (i==visited[v-1] and j==visited[v]):
                #            print(i)
                #            print(j)
                #            current_pheromone[i][j] = current_pheromone[i][j] + (1/ant_dict[ant]["distance"])
                #        print(current_pheromone)
                # row = current_pheromone[visited[v-1]]
                # print(row)
                # row[visited[v]] = row[visited[v]] + (1/ant_dict[ant]["distance"])
                current_pheromone[visited[v - 1]][visited[v]] = current_pheromone[visited[v - 1]][visited[v]] + (
                            1 / ant_dict[ant]["distance"])*ants
                current_pheromone[visited[v]][visited[v - 1]] = current_pheromone[visited[v]][visited[v - 1]] + (
                            1 / ant_dict[ant]["distance"])*ants

    for i in range(city):
        for j in range(city):
            pheromone_matrix[i][j] = (1-0.5) * pheromone_matrix[i][j] + current_pheromone[i][j]
    y_values.append(max1)
    print(y_values)
    print(pheromone_matrix)


def run_aco(n, city):
    for i in range(n):
        ant_dict = dict()

        for c in range(city):
            visited = []
            fringe = []
            path = dict()
            current_city = None
            distance_travelled = 0
            fringe.append(c)
            while fringe:
                moves = []
                current_city = fringe.pop(0)
                # print(current_city)
                visited.append(current_city)
                for adj in range(city):
                    if (adjacency_matrix[current_city][adj] == 1 and adj not in visited):
                        moves.append(adj)
                # print(moves)
                if (len(moves) != 0):
                    total_prob = total_allowed_distance(current_city, moves)
                    max = -1
                    next_city = 0;
                    for mv in moves:
                        prob = calculate_probability(current_city, mv, total_prob)

                        if max < prob:
                            max = prob
                            next_city = mv
                    # print(max)
                    # print(next_city)
                    distance_travelled = distance_travelled + distance_matrix[current_city][next_city]
                    fringe.append(next_city)
            last_city = visited[len(visited) - 1]
            if adjacency_matrix[last_city][visited[0]] == 1:
                visited.append(visited[0])
                distance_travelled = distance_travelled + distance_matrix[last_city][visited[0]]
            # print(visited)
            path["visited"] = visited
            path["distance"] = distance_travelled
            print(path)
            ant_dict[c] = path
        print(ant_dict)
        update_pheromone(ant_dict)
        x_values.append(i)


print("enter the number of iterations")
n = int(input())
print("enter the number of cities")
city = int(input())
print("enter number of ants")
ants = int(input())
inverse_distance_matrix =[]
distance_matrix = []

for i in range(city):
    dist =[]
    for j in range(city):
        dist.append(0)
    distance_matrix.append(dist)

for i in range(city):
    inv =[]
    dm = []
    for j in range(city):
        inv.append(0)
        if i==j:
            continue
        elif i<j:
            distance_matrix[i][j] = np.random.randint(1,15)
            distance_matrix[j][i] = distance_matrix[i][j]
    inverse_distance_matrix.append(inv)
distance_matrix = [[0, 14, 5, 4, 6, 5, 12, 8, 1, 12], [14, 0, 12, 3, 12, 14, 11, 8, 8, 6], [5, 12, 0, 2, 14, 7, 9, 13, 12, 3], [4, 3, 2, 0, 8, 5, 7, 9, 4, 11], [6, 12, 14, 8, 0, 4, 3, 5, 7, 2], [5, 14, 7, 5, 4, 0, 12, 12, 13, 6], [12, 11, 9, 7, 3, 12, 0, 12, 11, 2], [8, 8, 13, 9, 5, 12, 12, 0, 10, 6], [1, 8, 12, 4, 7, 13, 11, 10, 0, 9], [12, 6, 3, 11, 2, 6, 2, 6, 9, 0]]
#inverse_distance_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(city):
    for j in range(city):
        if distance_matrix[i][j] != 0:
            inverse_distance_matrix[i][j] = 1 / distance_matrix[i][j]
adjacency_matrix= []
pheromone_matrix = []
for i in range(city):
    adj = []
    phr = []
    for j in range(city):
        if i==j:
            adj.append(0)
            phr.append(0)
        else:
            adj.append(1)
            phr.append(1)
    adjacency_matrix.append(adj)
    pheromone_matrix.append(phr)
#adjacency_matrix = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
#pheromone_matrix = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
x_values =[]
y_values = []
print(min(distance_matrix))
#
run_aco(n, city)
plt.xlabel("Number of iterations")
plt.ylabel("Max tour length")
plt.title("Number of iterations vs Max tour length")
plt.plot(x_values,y_values)
plt.show()
print(distance_matrix)
print("coverged iteration: ",x_values[y_values.index(min(y_values))])