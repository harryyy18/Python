# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, try to figure out how to do the same thing using some other package

import win32com.client as win
speaker =win.Dispatch("SAPI.SpVoice")
list=["Rahul","Rohan","Harry"]

for i in list:
    print("Shoutout to"+i)
    
for name in list:
    names=name.split()
    shoutout=f"Shoutout to {names[0]}"
    speaker.Speak(shoutout)
    
print("Shoutout of all guys")        