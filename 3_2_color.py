import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Colors')
window.geometry('400x300')

# widgets 
ttk.Label(window, background = 'red').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#08F').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#4fc296').pack(expand = True, fill = 'both')

# exercise
# create a brownish color using hex values
ttk.Label(window, background = '#C50').pack(expand = True, fill = 'both')

# white and black
ttk.Label(window, background = '#000').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#888').pack(expand = True, fill = 'both')
ttk.Label(window, background = '#FFF').pack(expand = True, fill = 'both')

# run 
window.mainloop()