import tkinter as tk
from tkinter import ttk, font

# window
window = tk.Tk()
window.title('Styling')
window.geometry('400x300')

# print(font.families())

# style 
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('classic')

style.configure('new.TButton', foreground = 'green', font = ('Jokerman', 20))
style.map('new.TButton', 
	foreground = [('pressed', 'red'),('disabled', 'yellow')],
	background = [('pressed', 'green'), ('active', 'blue')])
style.configure('TFrame', background = 'pink')

# widgets 
label = ttk.Label(
	window, 
	text = 'A label\nAnd then type on another line', 
	background = 'red', 
	foreground = 'white',
	font = ('Jokerman', 20),
	justify = 'right')

label.pack()

button = ttk.Button(window, text = 'A button', style = 'new.TButton')
button.pack()

# exercise: 
# add a frame with a width and height and give it a pink background color

frame = ttk.Frame(window, height = 200, width = 100)
frame.pack()

# run 
window.mainloop()