import sys
import string
import webbrowser
from urllib.request import Request, urlopen, build_opener
from os import system
from urllib.error import HTTPError
from random import choice
from tkinter import *

class Rangur:

    def __init__(self):
        self.count = 0
        self.ext = ['.jpg', '.png'] #possible imgur extensions
        self.open = False #for testing, either open in browser or display to sdout
        self.size = 20 * 20

    def randomURL(self):
        chars = string.ascii_letters + string.digits #chars holds all the possible characters an imgur ID can be
        tempchar = [choice(chars) for n in range(5)]
        imgID = "".join(tempchar)
        url = "http://i.imgur.com/" + imgID
        return url

    def testURL(self, url):
        opener = build_opener()
        opener.add_headers = [("User-agent", "Mozilla/5.0")] #see http://webaim.org/blog/user-agent-string-history/
        try:
            opener.open(url)
            print("Success:: " + url)
            return True
        except KeyboardInterrupt:
            print("Error::Keyboard Interrupt")
            exit()
        except HTTPError:
            print("Error::HTTP Error:: " + url)
            return False

        #this whole testURL thing needs functionality for the placeholder image
        # req = Request(url)
        # data = None
        # try:
        #     data = urlopen(req)
        # except HTTPError as e:
        #     error_print("HTTP Error: "+str(e.code)+' '+image_name)
        # except URLError as e:
        #     error_print("URL Error: "+str(e.reason)+' '+image_name)
        #
        # if data:
        #     try:
        #         data = data.read();
        #
        #         # Check if placeholder image.
        #         if 'd835884373f4d6c8f24742ceabe74946' == hashlib.md5(data).hexdigest():
        #             print("Received placeholder image: "+image_name)
        #         # Check if image is above minimum size.
        #         elif self.size > sys.getsizeof(data):
        #             print("Received image is below minimum size threshold: "+image_name)
        #         else:
        #             return True
        #     except:
        #         print("data read failed")
        #         return False


    def main(self):
        while self.count <= 3: #set to whatever number you want
            url = self.randomURL()
            for cur_ext in self.ext:
                ext_url = url + cur_ext
                if(self.testURL(ext_url)):
                    print(ext_url)
                    self.count += 1

                    if self.open:
                        webbrowser.open(ext_url, new=0, autoraise=True)
                    else:
                        print("Not opened due to settings")
                else:
                    print("testURL failed for: " + ext_url)

if __name__ == '__main__':
    Rangur().main()
