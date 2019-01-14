from tkinter import *
from time import strftime, gmtime

root = Tk()
root.geometry('155x99')
root.title('BinClock')
root.resizable(False, False)
root.update()
clockTable = Canvas(root,width=root.winfo_width(), height=root.winfo_height(),bg='black')
clockLEDs = []
clockOffset = 4

switchLevel = 0
i = int(root.winfo_width()) - 3

while i - 20 > 0:                           #change row
    j = int(root.winfo_height()) - 3
    while j - 20 > 0:                       #change column
        clockLEDs.append(clockTable.create_rectangle(i, j, i - 20, j - 20, fill='grey'))
        clockTable.pack()
        j -= 24
    i -= 24
    switchLevel +=1
    if switchLevel == 2:
        i -= 4
        switchLevel = 0

clockTable.itemconfig(clockLEDs[0], fill='white')
clockTable.itemconfig(clockLEDs[0 + clockOffset*1], fill='white')
clockTable.itemconfig(clockLEDs[1 + clockOffset*5], fill='white')
nowTime = strftime("%H:%M:%S", gmtime())
parts = nowTime.split(":")
root.mainloop()
