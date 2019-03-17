# simulation of service station

import simpy

############CREATE MODEL############
# instantiate execution environment for simulation
environment = simpy.Environment()

# service station resource
charging_station = simpy.Resource(environment, capacity=1) ##CHANGE CAPACITY

# find interarrival times
interarrival_times = []
with open("interarrival_times.txt") as input_file:
    for line in input_file:
        line = line.strip('\n')
        interarrival_times.append(float(line))

print(interarrival_times)

#find service times
charging_times = []
with open("service_times.txt") as input_file:
    for line in input_file:
        line = line.strip('\n')
        charging_times.append(float(line))

print(charging_times)

# electric car process generator
def electric_car(environment, name, charging_station, arrival_time, charging_time):
     # trigger arrival event at charging station
     yield environment.timeout(arrival_time)

     # request charging bay resource
     print('%s arriving at %s' % (name, environment.now))
     with charging_station.request() as request:
         yield request

         waiting_time = environment.now - arrival_time
         print('%s waiting time %s' % (name, waiting_time))
         
         # charge car battery
         print('%s starting to charge at %s' % (name, environment.now))
         yield environment.timeout(charging_time)
         print('%s leaving at %s' % (name, environment.now))


arrival_time = 0
# simulate car processes
for i in range(len(interarrival_times)):
     arrival_time += interarrival_times[i]
     charging_time = charging_times[i]
     environment.process(electric_car(environment, 'Car %d' % i, charging_station, arrival_time, charging_time))
     #print('%s waiting time = %s' % (i, waiting_time))

environment.run()

