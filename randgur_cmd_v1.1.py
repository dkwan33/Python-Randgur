#!python3

import sys
import string, requests
import webbrowser
import urllib.request
from os import system
from urllib.error import HTTPError
from random import choice
from tkinter import *

def main():
    open_flag = False # can be set to false during testing to avoid opening in browser

    if len(sys.argv) >= 2:
        num_pics = int(sys.argv[1])
    else:
        num_pics = 3

    grab_some_images(open_flag, num_pics)

        
def grab_some_images(open_flag, num_pics):
    opener = urllib.request.build_opener()
    opener.add_headers = [("User-agent", "Mozilla/5.0")] #see http://webaim.org/blog/user-agent-string-history/

    count = 0
    while count < num_pics:
        url = rand_img_url()

        try:
            opener.open(url)
            print("Success:: " + url)
            count += 1
            if open_flag:
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

                
class Logger(object): #this class will write all stdout to both stdout and a log file
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open('stdout.log', "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): # for the python 3 flush command
        pass

if __name__ == '__main__':
    sys.stdout = Logger() #use Logger
    main()
