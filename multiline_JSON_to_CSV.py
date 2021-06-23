import csv
import json
import os

with open('devices.json',"r") as f:
    lines = []
    for line in f:
        lines.append(line)
        
key = json.loads(lines[0]) 
fieldnames=list(key.keys())

with open('employee_file2.csv', mode='a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if os.path.getsize("employee_file2.csv") == 0:
        writer.writeheader()
    
    for i in range(0,len(lines)):
        writer.writerow(json.loads(lines[i],encoding=True))
   

