#!python3

import sys
import string, requests
import webbrowser
from os import system
from urllib.request import build_opener
from urllib.error import HTTPError
from random import choice
import tkinter as tk


#CONSTANTS
LARGE_FONT = ("Verdana", 12)

class MainRandgur(tk.Tk):
    #This is all backend stuff, lay the foundation for the main app.
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew") #use grid to place widget, it is sticky to all 4 directions
        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise() #bring frame to the top for the user to see

class StartPage(tk.Frame): #use classes for each page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the start page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        # image = Image.open("testsloth.jpg")
        url = "http://inlandbikeco.com/WebRoot/Store5/Shops/f5754181-47ab-4a53-b022-734371542874/559D/F1C3/EA9B/1066/2E74/0A48/330B/CBFD/killswitch_stock_xs.jpg"
        image_bytes = urlopen(url).read()
        data_stream = io.BytesIO(image_bytes) #internal data file
        pil_image = Image.open(data_stream) #open as a PIL image object
        # optionally show image info
        # get the size of the image
        w, h = pil_image.size
        # split off image file name
        fname = url.split('/')[-1]
        sf = "{} ({}x{})".format(fname, w, h)

        # convert PIL image object to Tkinter PhotoImage object
        tk_image = ImageTk.PhotoImage(pil_image)

        # put the image onto the widget
        label = tk.Label(self, image=tk_image)
        label.pack(padx=5, pady=5)


        image = Image.open("testsloth.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.image = photo
        label.pack()

def main():
    app = MainRandgur()
    app.title("APP TITLE")
    app.mainloop()

def main_old():
    open = True # can be set to false during testing to avoid opening in browser

    if len(sys.argv) >= 2:
        num_pics = int(sys.argv[1])
    else:
        num_pics = 3

    opener = urllib.request.build_opener()
    opener.add_headers = [("User-agent", "Mozilla/5.0")] #see http://webaim.org/blog/user-agent-string-history/

    count = 0
    while count < num_pics:
        url = rand_img_url()

        try:
            opener.open(url)
            print("Success:: " + url)
            count += 1
            if open:
                webbrowser.open(url, new=0, autoraise=True)
        except KeyboardInterrupt:
            print("Error::Keyboard Interrupt")
            exit()
        except HTTPError:
            print("Error::HTTP Error:: " + url)
            pass

def rand_img_url():
    chars = string.ascii_letters + string.digits #chars holds all the possible characters an imgur ID can be
    # imgID = ''
    # for j in range(5):
    #     imgID += choice(chars)
    # ^ this is slow, see: http://docs.python-guide.org/en/latest/writing/structure/
    tempchar = [choice(chars) for n in range(5)]
    imgID = "".join(tempchar)
    url = "http://i.imgur.com/" + imgID
    return url

if __name__ == '__main__':
    main()
