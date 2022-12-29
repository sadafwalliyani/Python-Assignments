from tkinter import *

window = Tk()
window.title("welcome to my App")
# Label
lbl= Label(window, text="Happy New Year", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
window.geometry('500x200')
btn =Button(window, text="Click Me",bg="skyblue", fg="white" )
btn.grid(column=1, row=0)
def clicked():
    lbl.configure(text="""May this year bring new happiness,
     new goals, new achievements, 
     and a lot of new inspirations on your life.
     Ameeeeeeeeeeeen""")
btn =Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
    

window.mainloop()

