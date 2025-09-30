a = {"pens": 3, "notebooks": 12, "erasers": 0, "markers": 2, "scale":6, "bag":2}
total = 5

recored_list = []

for item, stock in a.items():
    if stock >= total:
        continue 
    recored_list.append(item)  

print("Reorder list:", recored_list)
