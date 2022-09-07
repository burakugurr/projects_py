import pyperclip
import pyshorteners
from tkinter import *

# Setting up the parameters for Tkinter
root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#2b4653")
root.iconbitmap("url.ico") # Using custom icon

url = StringVar()
url_addresses = StringVar()

# Function for shortening the URL
def url_shortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addresses.set(url_short)

# Function for copying the URL
def copy_url():
    url_short = url_addresses.get()
    pyperclip.copy(url_short)

# Setting up the buttons and their functionalities
Label(root, text= "My url Shortener", font="roboto").pack( pady= 10 )
Entry(root, textvariable=url).pack( pady=5 )

Button(root, text="Generate Short URL", command=url_shortener).pack( pady=7 )
Entry(root, textvariable= url_addresses).pack( pady= 5)

Button(root, text="Copy URL", command=copy_url).pack( pady= 5 )

root.mainloop()
