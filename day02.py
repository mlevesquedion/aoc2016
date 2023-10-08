# up, down, left, right
GRAPH1 = [
    [1, 4, 1, 2],
    [2, 5, 1, 3],
    [3, 6, 2, 3],
    [1, 7, 4, 5],
    [2, 8, 4, 6],
    [3, 9, 5, 6],
    [4, 7, 7, 8],
    [5, 8, 7, 9],
    [6, 9, 8, 9],
]

GRAPH2 = [
    [1, 3, 1, 1],
    [2, 6, 2, 3],
    [1, 7, 2, 4],
    [4, 8, 3, 4],
    [5, 5, 5, 6],
    [2, 10, 5, 7],
    [3, 11, 6, 8],
    [4, 12, 7, 9],
    [9, 9, 8, 9],
    [6, 10, 10, 11],
    [7, 13, 10, 12],
    [8, 12, 11, 12],
    [11, 13, 13, 13],
]

def simulate(graph):
    current = 5
    result = []
    for line in open('day02.txt'):
        for char in line.strip():
            current = graph[current-1]['UDLR'.index(char)]  
        result.append(hex(current).upper()[-1])
    return ''.join(result)

print('part 1:', simulate(GRAPH1))
print('part 2:', simulate(GRAPH2))
