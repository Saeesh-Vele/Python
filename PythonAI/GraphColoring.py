graph={'a':['b','c','d'], 'b':['a','c'] , 'c':['a','b','d'] , 'd':['a','c']}
colors=['red' , 'blue' , 'green']

def graph_coloring(graph):
    result={}
    for node in graph:
        used_colors={result[neighbour] for neighbour in graph[node] if neighbour in result}

        for color in colors:
            if color not in used_colors:
                result[node]=color
                break
    return result
print("Node Colors: " , graph_coloring(graph))
