# Author: Abdulrahman Jouhari
# Date: May 12, 2020

from math import inf, sqrt
from heapq import heappop, heappush
# For this model to work, the graph being input should have this structure:
# Class that is initialized to return the name using "self.name = name" and position using "self.position = (x, y)"
# location_name = class_name("location_name", x, y)

# Manhattan Heuristic Model
# Returns distance of gridded paths from start to finish by means of using straight lines on the x and y axis, ideal for shorter distances such as inner-city navigation
def manhattan_heuristic(start, end):
    x_distance = abs(start.position[0] - end.position[0])
    y_distance = abs(start.position[1] - end.position[1])
    return x_distance + y_distance

# Euclidean Heuristic Model
# Returns distance of direct digaonal line from start to end, ideal for larger distances such as worldwide navigation
def euclidean_heuristic(start, end):
    x_distance = abs(start.position[0] - end.position[0])
    y_distance = abs(start.position[1] - end.position[1])
    return sqrt((x_distance * x_distance) + (y_distance * y_distance))

# A-Star is a search algorithm that improves of Dijkstra's algorithm by giving it a sense of direction
def a_star(graph, start, end):
    distance_and_path = {}
  
    # It first assigns all the locations two attributes: a distance, and a path
    # The distance represents how far it is from the start vertex
    # The path represents the vertices it went through to arrive at there from the start vertex
    for vertex in graph:
        distance_and_path[vertex] = [inf, [start.name]]
    
    # The starting position gets assigned a distance of zero
    distance_and_path[start][0] = 0
  
    # It uses a heap queue to prioritize the location based on the distance from the start position, with the shortest distance being at the front of the queue
    vertices_available = [(0, start)]
    
    # Maintains the loop while there are both vertices that are unexplored and the end point has not been reached yet
    while vertices_available and distance_and_path[end][0] == inf:
        # Takes the first in the vertices_available queue, assigning the vertex to variables, then adding the neighbors of that vertex to the vertices_queue
        current_distance, current_vertex = heappop(vertices_available)
        
        for neighbor, edge_weight in graph[current_vertex]:
            # This is where the A-Star algorithm differs from Dijkstra's algorithm. It accounts for the distance between the neighbor and the end point when defining new_distance
            # You can adjust the heuristic to your preference
            new_distance = current_distance + edge_weight + euclidean_heuristic(neighbor, end)
            new_path = distance_and_path[current_vertex][1] + [neighbor.name]
            
            # It checks if the path from the current vertex to the neighbor is the neighbor's shortest path yet, if it is, it assigns the neighbor's distance attribute in the distance_and_path dictionary the new (shorter) distance
            # If it is the shortest path, it also assigns the neighbor's path attribute in the distance_and_path dictionary the path of the current vertex plus the neighbor's vertex
            if new_distance < distance_and_path[neighbor][0]:
                distance_and_path[neighbor][0] = new_distance
                distance_and_path[neighbor][1] = new_path
                heappush(vertices_available, (new_distance, neighbor))
    
    # Returns the path from the start vertex to the end vertex
    return distance_and_path[end][1]
