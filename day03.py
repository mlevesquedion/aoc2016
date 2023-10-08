def possible(triangle):
    a, b, c = sorted(triangle)
    return a + b > c

triangles = [tuple(map(int, line.split())) for line in open('day03.txt')]

# transposing 3-element lines gives 3 rows where each chunk of 3 elements is a triangle
# use sum to concatenate the rows
flat_triangles = sum([list(row) for row in zip(*triangles)], [])
vertical_triangles = [tuple(flat_triangles[i:i+3]) for i in range(0, len(flat_triangles), 3)]

print('part 1:', sum(map(possible, triangles)))
print('part 2:', sum(map(possible, vertical_triangles)))
