
# File setup
f = open("/home/hank/Documents/_scripts/etracker.txt", "r+")

device = input("Device Type: \n1) Laptop \n2)Desktop \n3)Printer \nInput: ")

#converting user input to lower for uniformity. // doesn't work for string conversion or whatever. 
#device = str(device.tolower)


print(device)
if device == 'L':
    print("you selected a LAPTOP")
    ws1 = input("Where did this device come from: ")
    ws2 = input("Where is this device going: ")
    f.write(device)
    f.write("\n")
    f.write(ws1)
    f.write("\n")
    f.write(ws2)
    f.write("\n")
elif device == 'D':
    print("You selected a DESKTOP")
    ws1 = input("Where did this device come from: ")
    ws2 = input("Where is this device going: ")
    f.write(device)
    f.write("\n")
    f.write(ws1)
    f.write("\n")
    f.write(ws2)
    f.write("\n")
elif device == 'P':
    print("You selected a PRINTER")
    ws1 = input("Where did this device come from: ")
    ws2 = input("Where is this device going: ")
    f.write(device)
    f.write("\n")
    f.write(ws1)
    f.write("\n")
    f.write(ws2)
    f.write("\n")
else:
    print("Error input")

f.close()



'''
with open ("etracker.txt", 'w') as f:
    f.write(device, ws1, ws2)
f.close()
'''
'''
with open("filename.txt", 'w') as f:
   f.write("dict = {'one': 1, 'two': 2}" + '\n')
'''