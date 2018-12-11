import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from Buttons import *
from Informations import *
import database as db


def getscreenwidth():
    w = win.winfo_screenwidth()
    return w

#Declare function to return screen hight
def getscreenheight():
    h = win.winfo_screenheight()
    return h

def tab1_action0():
    i = 0
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[i], db.retail[i]))
    i+=1
    print(i)

def tab1_action1():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[1], db.retail[1]))

def tab1_action2():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[2], db.retail[2]))

def tab1_action3():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[3], db.retail[3]))

def tab1_action4():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[4], db.retail[4]))

def tab1_action5():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[5], db.retail[5]))

def tab1_action6():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[6], db.retail[6]))

def tab1_action7():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[7], db.retail[7]))

def tab1_action8():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[8], db.retail[8]))

def tab1_action9():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[9], db.retail[9]))

def tab1_action10():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[10], db.retail[10]))

def tab1_action11():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[11], db.retail[11]))

def tab1_action12():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[12], db.retail[12]))

def tab1_action13():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[13], db.retail[13]))

def tab1_action14():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[14], db.retail[14]))

def tab1_action15():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[15], db.retail[15]))

def tab1_action16():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[16], db.retail[16]))

def tab1_action17():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[17], db.retail[17]))

def tab1_action18():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[18], db.retail[18]))

def tab1_action19():
    scr.insert('end', "%d %s $%.2f\n" %(counting(), db.title[19], db.retail[19]))

def get_total():
    total = 0 #initiliaze the total
    data = scr.get('1.0', 'end') #Save all data from screen
    splt = data.splitlines() #Split data into lines
    del splt[-1] #Delete the END line indicator
    l = len(splt) #Determine how many line exist
    for i in range (l):
        line = splt[i] #Append line by line to a variable using indicator
        line = line.split("$") #Concatenate line into two section
        conv = float(line[1]) #Take section one after the $ sign and append it to var while converting it to float
        total += conv  #Add the converted float to the total
    return total #Return total

def ttl_action():
    #Change the total label to the following configuration.
    ttl_label.configure(text="$%.2f" % get_total())

count = 0
def counting():
    global count
    count += 1
    return count

indx = 0
c = 0
r = 0
def slice_title():
    global indx
    title = db.label[indx]
    indx+=1
    return title

def config_button(self):
    global c
    global r
    self.grid(column=c, row=r)
    self.configure(font = 'bold',background = "green", text=slice_title(), height = 3, width = 13)
    r +=1
    if r == 7:
        r = 0
        c+= 1

#function that clear all the data from the scrolled text box
def clear_screen():
    scr.delete('1.0', 'end') #Delete from line 1 character 0 to the end
    ttl_action() #Call the total function to recalculate the total

#Display the following information to the user:
    #User Name or ID
    #Date/Time
    #Transaction number
def info():
    def date():
        print()
    def time():
        info_bar.config(text=clock.get_long_time())
        info_bar.after(200,info)
    time()


#Create instance
win = tk.Tk()

#Add Title
win.title("POS")

#Make window fit the size of the screen
win.geometry('%dx%d+0+0' % (getscreenwidth(),getscreenheight()))

#Disable resizing the GUI
win.resizable(False, False)

#Create an instance of tab Control
tabcontrol = ttk.Notebook(win)

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", bg="black")

#Setting the tab size
tabcontrol.place(width=660, height=getscreenheight()-90 )


#Create Three Tabs and config each one of them
tab1 = tk.Frame(tabcontrol)
tab1.configure(bg= "green")
tabcontrol.add(tab1, text= f'{"Breakfast": ^80s}')
tab2 = tk.Frame(tabcontrol)
tabcontrol.add(tab2, text= f'{"Lunch": ^80s}')
tab3 = tk.Frame(tabcontrol)
tabcontrol.add(tab3, text= f'{"Dinner": ^80s}')

#Create a info bar
info_bar = tk.Label(win)
info_bar.place(x = 0, y = 640)


#Create a Scrolled text as a display to output the items selected
scr = scrolledtext.ScrolledText(win, width = 45, height = 30)
scr.pack(side = "right")

#Setting up Clear Button
time_label = tk.Label(win)
time_label.place(x = 760, y = 300)
time_label.configure(font = 'currier 26 bold', background = "green")

down_button = tk.Button(win)
down_button.place(x = 760, y = 400)
down_button.configure(font = 'currier 26 bold', background = "green", text="DOWN", command=clear_screen)

clr_button = tk.Button(win)
clr_button.place(x = 760, y = 500)
clr_button.configure(font = 'currier 26 bold', background = "green", text="hi", command=clear_screen)


#Setting up Total Button
ttl_button = tk.Button(win)
ttl_button.place(x = 900, y = 610)
ttl_button.configure(font = 'currier 26 bold', background = "blue", text="Total",  command =ttl_action)

#Setting up Total Label
ttl_label = tk.Label(win)
ttl_label.place(x = 1100, y = 610)
ttl_label.configure(font = 'currier 26 bold', text=get_total())




#Setting Button 0
b0 = tk.Button(tab1)
b0.configure(command=tab1_action0)
config_button(b0)

b1 = tk.Button(tab1)
b1.configure(command=tab1_action1)
config_button(b1)

b2 = tk.Button(tab1)
b2.configure(command=tab1_action2)
config_button(b2)

b3 = tk.Button(tab1)
b3.configure(command=tab1_action3)
config_button(b3)

b4 = tk.Button(tab1)
b4.configure(command=tab1_action4)
config_button(b4)

b5 = tk.Button(tab1)
b5.configure(command=tab1_action5)
config_button(b5)

b6 = tk.Button(tab1)
b6.configure(command=tab1_action6)
config_button(b6)

b7 = tk.Button(tab1)
b7.configure(command=tab1_action7)
config_button(b7)

b8 = tk.Button(tab1)
b8.configure(command=tab1_action8)
config_button(b8)

b9 = tk.Button(tab1)
b9.configure(command=tab1_action9)
config_button(b9)

b10 = tk.Button(tab1)
b10.configure(command=tab1_action10)
config_button(b10)

b11 = tk.Button(tab1)
b11.configure(command=tab1_action11)
config_button(b11)

b12 = tk.Button(tab1)
b12.configure(command=tab1_action12)
config_button(b12)

b13 = tk.Button(tab1)
b13.configure(command=tab1_action13)
config_button(b13)

b14 = tk.Button(tab1)
b14.configure(command=tab1_action14)
config_button(b14)

b15 = tk.Button(tab1)
b15.configure(command=tab1_action15)
config_button(b15)

b16 = tk.Button(tab1)
b16.configure(command=tab1_action16)
config_button(b16)

b17 = tk.Button(tab1)
b17.configure(command=tab1_action17)
config_button(b17)

b18 = tk.Button(tab1)
b18.configure(command=tab1_action18)
config_button(b18)

b19 = tk.Button(tab1)
b19.configure(command=tab1_action19)
config_button(b19)

b20 = tk.Button(tab1)
b20.configure(command=tab1_action19)
config_button(b20)

#Setting Button 0
b0 = tk.Button(tab2)
b0.grid(column=0, row=0)
b0.configure(background = "red", text=db.title[0], height=8, width=30, command=tab1_action0)

b1 = tk.Button(tab2)
b1.grid(column=0, row=1)
b1.configure(background = "red", text=db.title[1], height=8, width=30, command=tab1_action0)

b2 = tk.Button(tab2)
b2.grid(column=0, row=2)
b2.configure(background = "red", text=db.title[2], height=8, width=30, command=tab1_action0)

b3 = tk.Button(tab2)
b3.grid(column=0, row=3)
b3.configure(background = "red", text=db.title[3], height=8, width=30, command=tab1_action0)

b4 = tk.Button(tab2)
b4.grid(column=0, row=4)
b4.configure(background = "red", text=db.title[4], height=8, width=30, command=tab1_action0)

b5 = tk.Button(tab2)
b5.grid(column=1, row=0)
b5.configure(background = "red", text=db.title[5], height=8, width=30)

b6 = tk.Button(tab2)
b6.grid(column=1, row=1)
b6.configure(background = "red", text=db.title[6], height=8, width=30)

b7 = tk.Button(tab2)
b7.grid(column=1, row=2)
b7.configure(background = "red", text=db.title[7], height=8, width=30)

b8 = tk.Button(tab2)
b8.grid(column=1, row=3)
b8.configure(background = "red", text=db.title[8], height=8, width=30)

b9 = tk.Button(tab2)
b9.grid(column=1, row=4)
b9.configure(background = "red", text=db.title[9], height=8, width=30)

b10 = tk.Button(tab2)
b10.grid(column=2, row=0)
b10.configure(background = "red", text=db.title[10], height=8, width=30)

b11 = tk.Button(tab2)
b11.grid(column=2, row=1)
b11.configure(background = "red", text=db.title[11], height=8, width=30)

b12 = tk.Button(tab2)
b12.grid(column=2, row=2)
b12.configure(background = "red", text=db.title[12], height=8, width=30)

b13 = tk.Button(tab2)
b13.grid(column=2, row=3)
b13.configure(background = "red", text=db.title[13], height=8, width=30)

b14 = tk.Button(tab2)
b14.grid(column=2, row=4)
b14.configure(background = "red", text=db.title[14], height=8, width=30)

b15 = tk.Button(tab2)
b15.grid(column=3, row=0)
b15.configure(background = "red", text=db.title[15], height=8, width=30)

b16 = tk.Button(tab2)
b16.grid(column=3, row=1)
b16.configure(background = "red", text=db.title[16], height=8, width=30)

b17 = tk.Button(tab2)
b17.grid(column=3, row=2)
b17.configure(background = "red", text=db.title[17], height=8, width=30)

b18 = tk.Button(tab2)
b18.grid(column=3, row=3)
b18.configure(background = "red", text=db.title[18], height=8, width=30)

b19 = tk.Button(tab2)
b19.grid(column=3, row=4)
b19.configure(background = "red", text=db.title[19], height=8, width=30)


#Setting Button 0
b0 = tk.Button(tab3)
b0.grid(column=0, row=0)
b0.configure(background = "yellow", text=db.title[0], height=8, width=30)

b1 = tk.Button(tab3)
b1.grid(column=0, row=1)
b1.configure(background = "yellow", text=db.title[1], height=8, width=30)

b2 = tk.Button(tab3)
b2.grid(column=0, row=2)
b2.configure(background = "yellow", text=db.title[2], height=8, width=30)

b3 = tk.Button(tab3)
b3.grid(column=0, row=3)
b3.configure(background = "yellow", text=db.title[3], height=8, width=30)

b4 = tk.Button(tab3)
b4.grid(column=0, row=4)
b4.configure(background = "yellow", text=db.title[4], height=8, width=30)

b5 = tk.Button(tab3)
b5.grid(column=1, row=0)
b5.configure(background = "yellow", text=db.title[5], height=8, width=30)

b6 = tk.Button(tab3)
b6.grid(column=1, row=1)
b6.configure(background = "yellow", text=db.title[6], height=8, width=30)

b7 = tk.Button(tab3)
b7.grid(column=1, row=2)
b7.configure(background = "yellow", text=db.title[7], height=8, width=30)

b8 = tk.Button(tab3)
b8.grid(column=1, row=3)
b8.configure(background = "yellow", text=db.title[8], height=8, width=30)

b9 = tk.Button(tab3)
b9.grid(column=1, row=4)
b9.configure(background = "yellow", text=db.title[9], height=8, width=30)

b10 = tk.Button(tab3)
b10.grid(column=2, row=0)
b10.configure(background = "yellow", text=db.title[10], height=8, width=30)

b11 = tk.Button(tab3)
b11.grid(column=2, row=1)
b11.configure(background = "yellow", text=db.title[11], height=8, width=30)

b12 = tk.Button(tab3)
b12.grid(column=2, row=2)
b12.configure(background = "yellow", text=db.title[12], height=8, width=30)

b13 = tk.Button(tab3)
b13.grid(column=2, row=3)
b13.configure(background = "yellow", text=db.title[13], height=8, width=30)

b14 = tk.Button(tab3)
b14.grid(column=2, row=4)
b14.configure(background = "yellow", text=db.title[14], height=8, width=30)

b15 = tk.Button(tab3)
b15.grid(column=3, row=0)
b15.configure(background = "yellow", text=db.title[15], height=8, width=30)

b16 = tk.Button(tab3)
b16.grid(column=3, row=1)
b16.configure(background = "yellow", text=db.title[16], height=8, width=30)

b17 = tk.Button(tab3)
b17.grid(column=3, row=2)
b17.configure(background = "yellow", text=db.title[17], height=8, width=30)

b18 = tk.Button(tab3)
b18.grid(column=3, row=3)
b18.configure(background = "yellow", text=db.title[18], height=8, width=30)

b19 = tk.Button(tab3)
b19.grid(column=3, row=4)
b19.configure(background = "yellow", text=db.title[19], height=8, width=30)


info()

#Start GUI
win.mainloop()
