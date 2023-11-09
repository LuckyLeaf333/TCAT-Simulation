from PassengerClass import Passenger
import csv

with open('Passenger.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader)
    passenger_list = []
    for row in reader:
        attribute = []
        [attribute.append(int(i)) for i in row[0].split(",")]
        
        passenger_list.append(Passenger(attribute[0], attribute[1]))

