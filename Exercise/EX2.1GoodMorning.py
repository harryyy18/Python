#Program will the user according to the time using time module

import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print("Hours:",hour)
minute=int(time.strftime('%M'))
print("Minutes:",minute)
second=int(time.strftime('%S'))
print("Seconds:",second)
if(hour>=6 and hour<12):
    print("Good Moring")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour<19):
    print("Good Evening")
else:
    print("Good Night")    
            
