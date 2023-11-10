from PassengerClass import Passenger
from BusClass import Bus
from RouteClass import Route
import csv
import ast

with open('Passenger.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader)
    passenger_list = []
    for row in reader:
        attribute = []
        [attribute.append(int(i)) for i in row[0].split(",")]
        
        passenger_list.append(Passenger(attribute[0], attribute[1]))

with open('Bus.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader)
    bus_list = []
    for row in reader:
        attribute = []
        [attribute.append(int(i)) for i in row[0].split(",")]
        
        bus_list.append(Bus(attribute[0], attribute[1], attribute[2], attribute[3]))

# with open('route.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     next(reader)
#     dict = {}
#     for row in reader:
#         nodes = list(map(int, row[0].strip('[]').split(', ')))
#         edges = list(map(int, row[1].strip('[]').split(', ')))
#         number = int(row[2])
#         positions = list(map(int, row[3].strip('[]').split(', ')))
#         times = list(map(int, row[4].strip('[]').split(', ')))

#         route_obj = Route(nodes, edges, number, positions, times)
#         dict[number] =route_obj



