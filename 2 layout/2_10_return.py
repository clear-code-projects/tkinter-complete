import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
	frame = ttk.Frame(master = parent)

	# grid layout 
	frame.rowconfigure(0, weight = 1)
	frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')

	# widgets
	ttk.Label(frame, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
	ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')

	return frame

class Segment(ttk.Frame):
	def __init__(self, parent, label_text, button_text, exercise_text):
		super().__init__(master = parent)

		# grid layout 
		self.rowconfigure(0, weight = 1)
		self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
		
		# widgets 
		ttk.Label(self, text = label_text).grid(row = 0, column = 0, sticky = 'nsew')
		ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nsew')
		self.create_exercise_box(exercise_text).grid(row = 0, column = 2, sticky = 'nsew')

		self.pack(expand = True, fill = 'both', padx = 10, pady = 10)

	def create_exercise_box(self, text):
		frame = ttk.Frame(master = self)
		ttk.Entry(frame).pack(expand = True, fill = 'both')
		ttk.Button(frame, text = text).pack(expand = True, fill = 'both')
		return frame

# window
window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

# widgets 
# create_segment(window, 'label', 'button').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'test', 'click').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'hello', 'test').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'bye', 'launch').pack(expand = True, fill = 'both', padx = 10, pady = 10)
# create_segment(window, 'last one', 'exit').pack(expand = True, fill = 'both', padx = 10, pady = 10)


Segment(window, 'label', 'button', 'test')
Segment(window, 'test', 'click', 'something else')
Segment(window, 'hello', 'test', '123')
Segment(window, 'bye', 'launch', '')
Segment(window, 'last one', 'exit', 'end')

# exercise
# create a smaller widget inside of the segment class using a function/method:
# it should be a container that has an entry field and a button stacked on top of each other 
# the button text should be set via the parameters
# all of this should be on the third column

# run
window.mainloop()