"""
Code from: https://winterflower.github.io/2016/03/27/writing-your-first-simpy-simulation/
"""

import simpy
import random

def bus(simpy_environment):
    '''Simple Simpy bus simulation'''
    driving_duration = 5 #time taken to drive between two stops in this neighbourhood
    stopping_duration = 10
    for i in range(15):
        print('Start driving to bus stop %d at time %d' % (i, simpy_environment.now ))
        yield simpy_environment.timeout(driving_duration)
        print('Stopping to pick up commuters at bus stop %d at time %d' % (i, simpy_environment.now ))
        yield simpy_environment.timeout(stopping_duration)

env = simpy.Environment() #create the SimPy environment
env.process( bus(env) ) # create an instance of the Bus process
env.run()