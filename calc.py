import tkinter as tk
'''imports tk inter module 
tk is an alias for easy acess'''
#button click handler
def press(v):
    entry.insert(tk.END,v)
    '''called when a number or operator button is clicked
    inserts the pressed value at the end of the entry widget'''
def clear():
    entry.delete(0,tk.END)
    '''called when clear button is clicked
    deletes all text from the entry widget'''

def calc():
    try:
        result=eval(entry.get())
        '''entry.get retrives the expression (eg 5+3)
        eval evaluates the string as a python expression'''
        entry.delete(0,tk.END)#clears the screen
        entry.insert(0,result)#displays the result
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"invalid expression")
        '''handles invalid expressions eg(5++)
        displays appropriate message instead of crashing'''

#main window creation
root=tk.Tk()#creates main application window

root.title("Calculator")#sets window title

root.config(bg="#1e1e1e")#sets background color

root.resizable(False,False)#prevents window resizing

#entry widget (displaying screen)for displaying input and output
entry=tk.Entry(
    root,
    font=("times new roman",20),
    bg="#2d2d2d",
    fg="#ffffff",
    bd=0,
    justify="right"
)

'''text input field
acts as the calculator display
right alligned for better calculation look'''

entry.grid(row=0,column=0,columnspan=4,padx=10,pady=12,ipady=10)
'''places entry at top
columnspan 4 to span across all columns'''

#button labels
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
    'C'
]

'''represents calculator buttons 
stored in a list to reduce repetitive code'''

#dynamic button creation
r=1
c=0
'''rows and columns counters for grid layout'''

for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    '''if button is '=' call calc function
    otherwise call press with button value
    lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        command=cmd,
        font=("calibri",14),
        width=5,
        height=2,
        bg="#ff9500" if b in {'/','*','-','+','='} else "#3a3a3a",
        fg="#ffffff",
        bd=0,
    ).grid(row=r,column=c,padx=6,pady=6)

    c+=1
    if c==4:
        r+=1
        c=0
    '''moves to next row after 4 buttons'''

#clear button spans all columns
tk.Button(
    root,
    text='C',
    command=clear,
    font=("calibri",14),
    bg="#ff3b30",
    bd=0,
    width=23,
    height=2,
).grid(row=r,column=0,columnspan=4,padx=6,pady=6)    

root.mainloop()