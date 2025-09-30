queue = ['harsh', 'harshil', 'yash', 'abhi', 'gopal', 'henish', 'parthu']
bus = []

while len(bus) < 5 and len(queue) > 0:
    person = queue.pop(0)   
    bus.append(person)  
 
print("Seated:", bus)
print("Left in queue:", queue)
