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

# Define the file path
file_path = 'test.html'

#stores html
new_content = BeautifulSoup('<div class="col-sm-4"><img src="img/communications.png" class="img-fluid" alt="testitestitesti"><p>Testi</p><p>TestingtheTest</p></div>', 'html.parser')

#method for writing to file 
def callback():
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    body_tag = soup.find('body')
    if body_tag:
        body_tag.append(new_content.div)
    
    with open(file_path, 'w') as file:
        file.write(soup.prettify(formatter=lambda s: s.replace("/>", ">")))


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
