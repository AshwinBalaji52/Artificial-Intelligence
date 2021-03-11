class Vertex():
    def __init__(self, parent=None, location=None):
        self.parent = parent
        self.location = location
        self.g = 0
        self.h = 0
        self.f = 0
        
    def __eq__(self, other):
        return self.location == other.location
    
def Astar(graph, source, destination):
    
    initial_vertex = Vertex(None, source)
    initial_vertex.g = initial_vertex.h = initial_vertex.f = 0
    final_vertex = Vertex(None, destination)
    final_vertex.g = final_vertex.h = final_vertex.f = 0
    open_list = []
    closed_list = []
    
    open_list.append(initial_vertex)
    
    while len(open_list) > 0:
        
        current_vertex = open_list[0]
        current_index = 0
        
        for index,value in enumerate(open_list):
            
            if value.f < current_vertex.f:
                current_vertex = value
                current_index = index
                
        open_list.pop(current_index)
        closed_list.append(current_vertex)
        
        if current_vertex == final_vertex:
            path = []
            current = current_vertex
            
            while current is not None:
                path.append(current.location)
                current = current.parent
            return path[::-1]
        
        children = []
        
        for new_location in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            vertex_location = (current_vertex.location[0] + new_location[0], current_vertex.location[1] + new_location[1])
            
            if vertex_location[0] > (len(graph) - 1) or vertex_location[0] < 0 or vertex_location[1] > (
                    len(graph[len(graph) - 1]) - 1) or vertex_location[1] < 0:
                continue
            
            if graph[vertex_location[0]][vertex_location[1]] != 0:
                continue
            new_vertex = Vertex(current_vertex, vertex_location)
            children.append(new_vertex)
            
        for child in children:
            for closed_child in closed_list:
                
                if child == closed_child:
                    continue
            child.g = current_vertex.g + 1
            
            child.h = ((child.location[0] - final_vertex.location[0]) ** 2) + (
                    (child.location[1] - final_vertex.location[1]) ** 2)
            
            child.f = child.g + child.h
            for open_vertex in open_list:
                
                if child == open_vertex and child.g > open_vertex.g:
                    continue
            open_list.append(child)
            
def main():
    '''
    Path exist == 0
    Path doesn't exist == 1
    '''

    graph = [[0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
             [0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
             [0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
             [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
             [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 0, 1, 1, 1, 0, 0]]   
    
    source = (0, 0)
    destination = (9,9)
    path = Astar(graph, source, destination)
    print("\n\t\t\t\t\tA-STAR PATH PLANNING\n")
    print("Route Traversal:", path[0], "-->", path[1], "-->", path[2], "-->"
          , path[3], "-->", path[4], "-->", path[5], "-->", path[6], "-->"
          , path[7], "-->", path[8], "-->", path[9])
    
if __name__ == '__main__':
    main()