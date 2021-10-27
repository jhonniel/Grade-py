cell = input ("Enter Cellular Number: ")
Smart = '13,14,20,21,28,29,30'
TNT = '09,08,10,11,12,18,19'
Sun ='22,23,33,32'
Globe= '15,16,17,25,26,27'
TM = '03,04,05,06,07'
Red = '01,02,24'
while True:
    if len(cell)==11 and cell.isnumeric():
        break
    else:
        cell = input ("Enter Cell Number Again:")
num = cell[2]+cell[3]
if num in Smart:
    print ("The number",cell," belongs to Smart.")
elif num in TNT:
    print ("The number",cell,"belongs to TNT.")
elif num in Sun:
    print ("The number",cell," belongs to Sun.")
elif num in Globe:
    print ("The number ",cell,"belongs to Globe.")
elif num in TM:
    print ("The number ",cell," belongs to TM.")
elif num in Red:
    print ("The number ",cell," belongs to Red.")
else:
    print ("The number ",cell," is not recognized.")
