# simulation of service station

import simpy
import statistics

# instantiate execution environment for simulation
environment = simpy.Environment()

# find model info
model_info = []
with open("model_inputs.txt") as input_file:
  for line in input_file:
        line = line.strip('\n')
        model_info.append((line))

capacity = int(model_info[1]) # get environment capacity

# service station resource
service_station = simpy.Resource(environment, capacity) 

# find interarrival times
interarrival_times = []
with open("interarrival_times.txt") as input_file:
    for line in input_file:
        line = line.strip('\n')
        interarrival_times.append(float(line))


#find service times
service_times = []
with open("service_times.txt") as input_file:
    for line in input_file:
        line = line.strip('\n')
        service_times.append(float(line))


# statistics initialization
waiting_times = []
queue_lengths = []
idle_times = []

print("\nEach",model_info[2],"will be serviced by",model_info[0],"\n")

# entity process generator
def entity(environment, name, service_station, arrival_time, service_time):
     # trigger arrival event at charging station
     yield environment.timeout(arrival_time)

     # request charging bay resource
     print(model_info[2],'%s arriving at %3.1f' % (name, environment.now))
     with service_station.request() as request:
         yield request

         waiting_time = environment.now - arrival_time
         print(model_info[2],'%s waiting time %3.1f' % (name, waiting_time))
         
         # servicing entity
         print(model_info[2],'%s starting service at %3.1f' % (name, environment.now))
         idle_times.append(environment.now) 
         yield environment.timeout(service_time)
         
          
         print(model_info[2],'%s leaving at %3.1f' % (name, environment.now))
         idle_times.append(environment.now)
         
         # collect waiting times
         waiting_times.append(waiting_time)
         queue_lengths.append(len(service_station.queue))


arrival_time = 0
# simulate entity processes
for i in range(len(interarrival_times)):
     arrival_time += interarrival_times[i]
     service_time = service_times[i]
     environment.process(entity(environment, '%d' % i, service_station, arrival_time, service_time))


environment.run()

#calculate total idle time
idle_total = 0
i = 1
while (i < len(idle_times)-1):
  idle_total+=idle_times[i+1]-idle_times[i]
  i=i+2

print("\n\033[4mSummary\033[0m")
print("Total time elapsed =",idle_times[-1],"minutes")
print ("Minumum queue length =",min(queue_lengths))
print ("Maximum queue length =",max(queue_lengths))

print ("Total idle time for the resource = %3.2f minutes" % idle_total)
print("Resource utilization percent =",100-(idle_times[-1]-idle_total),"%")

print ("Total queue time = %3.2f minutes" % sum(waiting_times))
print ("Mean waiting time = %3.2f minutes" % statistics.mean(waiting_times))
print ("Variance of waiting time = %3.2f" % statistics.variance(waiting_times))
