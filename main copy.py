import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Text
from bs4 import BeautifulSoup
from html.parser import HTMLParser

root = tk.Tk()
root.title('PortfolioEditor')

window_width = 300
window_height = 200
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# place a label on the root window
message = ttk.Label(root, text="Make a new Portfolio entry.")
message.pack()

text = Text(root, height=8)
text.pack()

#preview text placement.line 1 character 0
text.insert('1.0', 'Write your entry here')

#retrieves the contents of a text widget
text_content = text.get('1.0','end')

#stores html
html_str = """<div class="col-sm-4">
            <img src="img/communications.png" class="img-fluid" alt="Simple image of a megaphone">
            <p>Communications</p>
            <p>Streamlining the internal digital communications of my degree programme</p>
        </div>"""
#method for writing to file 
def callback():
    with open("test.html", "a") as file:
        file.write(html_str)
    with open("test.html") as file: 
        contents = file.read() 
        print(contents) 
#button function
write_button = ttk.Button(
   root, 
   text="Write html", 
   command=callback
)
#button appearance
write_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


# keep the window displaying
root.mainloop()


#next time look into a html editing python library like beautiful soup
