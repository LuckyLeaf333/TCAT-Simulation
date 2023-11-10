import pandas
import Route

route30Data = pandas.read_csv('Route30Locations.csv')
print(route30Data)
print(route30Data.columns)

nodes = []
edges = []
positions = [(0, 0)]
times = [5, 6, 7, 9, 8, 9, 5]

for i in range(1, len(route30Data.index) + 1):
    nodes.append(i)
    if i > 1:
        edges.append((i-1, i))
    positions.append((route30Data.iloc[i-1, 1], route30Data.iloc[i-1, 2]))
edges.append((1, len(route30Data.index)))
print(nodes)
print(edges)
print(positions)

testRoute = Route.Route(nodes, edges, 30, positions, times)
testRoute.show()