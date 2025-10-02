queue = ['harsh', 'harshil', 'yash', 'abhi', 'gopal', 'henish', 'parthu']
buslist = []

while len(buslist) < 5 and len(queue) > 0:
    person = queue.pop(0)   
    buslist.append(person)  
 
print("Seated:", buslist)
print("Left in queue:", queue)
