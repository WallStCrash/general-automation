"""
    Title:     PriceCheck-GitHub-Edit.py
    Author:    @WallStCrash
    Date:      19.02.2022
    
    Purpose:   This is a Python script to automate checking prices on websites.
    
    Notes:     Keep any eye on the URL of the item you are looking at as they can potentially change
                                       
"""
# Import libraries and dependencies

from requests_html import HTMLSession
import tkinter as tk 

# Define get_price function for this script
def get_price(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep = 1)

    global product     # Need product dictionary defined outside of get_price too

    product={
        'title': r.html.xpath("xpath-to-html-element", first=True).text,
        'price': r.html.xpath("xpath-to-html-element", first=True).text
    }

get_price("url of object page")

txtPrice = product.get('price').replace("£", '')
numPrice = float(txtPrice)
desirePrice = 100       # enter price threshold you want to be alerted for

if numPrice < desirePrice:
    root = tk.Tk() 
    root.title("Price Check Alert")
    canvas1 = tk.Canvas(root, width = 500, height = 500)
    canvas1.pack()
    label1 = tk.Label(root, text='\nGood price available now on:\nitemname!', fg="yellow", bg="blue")
    canvas1.create_window(250, 250, window=label1)
    root.mainloop()
elif numPrice > desirePrice:
    exit()
