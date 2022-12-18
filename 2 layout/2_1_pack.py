import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

# widgets 
label1 = ttk.Label(window, text = 'First label', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Last of the labels', background = 'green')
button = ttk.Button(window, text = 'Button')

# layout 
label1.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)
label2.pack(side = 'left', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')

# run
window.mainloop()