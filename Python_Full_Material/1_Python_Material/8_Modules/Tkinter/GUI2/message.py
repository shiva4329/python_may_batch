import tkinter as tk
master = tk.Tk()
data = "SUCCESS ALWAYS FOLLOWS HARDWORK"
msg = tk.Message(master, text = data)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tk.mainloop()
