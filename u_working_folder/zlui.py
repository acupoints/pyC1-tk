import tkinter as tk
# root = tk.Tk()
# root.iconbitmap('pyc.ico')
# root.title("Hello, World!")
# root.overrideredirect(True)
# root.mainloop()
# from tkinter import *




def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

def main(root):
    # root = tk.Tk()
    # root.iconbitmap('pyc.ico')
    # root.title("Hello, World!")
    root.overrideredirect(True)
    # window.title('my window')
    root.configure(background="#007501")
    root.geometry('500x500')
    root.resizable(0,0)
    button_exit = tk.Button(root, text='Exit', relief=tk.FLAT, command=root.quit)
    button_exit.pack()
    # B1 = tk.Button(root, text ="FLAT", relief=tk.FLAT )
    # B2 = tk.Button(root, text ="RAISED", relief=tk.RAISED )
    # B3 = tk.Button(root, text ="SUNKEN", relief=tk.SUNKEN )
    # B4 = tk.Button(root, text ="GROOVE", relief=tk.GROOVE )
    # B5 = tk.Button(root, text ="RIDGE", relief=tk.RIDGE )
    # B1.pack()
    # B2.pack()
    # B3.pack()
    # B4.pack()
    # B5.pack()
    root.geometry("650x480+500+300")
    root.bind('<Button-1>', SaveLastClickPos)
    root.bind('<B1-Motion>', Dragging)
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    lastClickX = 0
    lastClickY = 0
    main(root)