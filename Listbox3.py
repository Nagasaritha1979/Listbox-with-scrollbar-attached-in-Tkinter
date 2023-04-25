from tkinter import *
    
win=Tk()
        

frame1=Frame(win)
frame1.pack()
scrollbar1=Scrollbar(frame1,orient=VERTICAL)
scrollbar1.pack(side=RIGHT,fill=Y)
  
listbox1=Listbox(frame1,width=50,yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)

for items in range(100):
    listbox1.insert(END,items)
    

listbox1.pack()
win.mainloop()
