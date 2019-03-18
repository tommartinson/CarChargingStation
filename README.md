# Discrete Event Simulator
This is a discrete event simulator used to model any generic discrete event simulation.

Inputs: Given to model through 3 different txt files.

model_inputs.txt: 
  Line 1 of this file is the server name.
  Line 2 of this file is the server capacity.
  Line 3 of this file is the entity name.
  
  Example:
    Jamba Juice
    
    1
    
    customer

interarrival_times.txt: 
  Each line of this file represents an interr-arrival time between entities.
  
  Example: 
    0 
    
    2.3
    
    4.1 
    
    1.1 
    
    0.8 
    
    2.1
    

service_times.txt:
  Each line of this file represents a service time for an entity.
  
  Example:
    2.0 
    
    3.2 
    
    1.2 
    
    2.9 
    
    1.2 
    
    0.8 
    
    
Output of this example:
  Each customer will be serviced by Jamba Juice

customer 0 arriving at 0.0

customer 0 waiting time 0.0

customer 0 starting service at 0.0

customer 0 leaving at 2.0

customer 1 arriving at 2.3

customer 1 waiting time 0.0

customer 1 starting service at 2.3

customer 1 leaving at 5.5

customer 2 arriving at 6.4

customer 2 waiting time 0.0

customer 2 starting service at 6.4

customer 3 arriving at 7.5

customer 2 leaving at 7.6

customer 3 waiting time 0.1

customer 3 starting service at 7.6

customer 4 arriving at 8.3

customer 5 arriving at 10.4

customer 3 leaving at 10.5

customer 4 waiting time 2.2

customer 4 starting service at 10.5

customer 4 leaving at 11.7

customer 5 waiting time 1.3

customer 5 starting service at 11.7

customer 5 leaving at 12.5


Summary

Total time elapsed = 12.5 minutes

Minumum queue length = 0

Maximum queue length = 2

Total idle time for the resource = 1.20 minutes

Resource utilization percent = 88.7 %

Total queue time = 3.60 minutes

Mean waiting time = 0.60 minutes

Variance of waiting time = 0.88

