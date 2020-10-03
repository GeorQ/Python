time = input()
new_time = ""
typet = time[-2]
if typet == "A":
    new_time = time[0:8]
else: 
    if int(time[0:2] == "12"):
        new_time = "00:" + time[3:8]
    else:
        new_time = str(int(time[0:2]) + 12) + time[2:8]  
print(new_time)