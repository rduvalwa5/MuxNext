'''
Created on Feb 5, 2017

@author: rduvalwa2
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createAlbumWidgets()
        
    def createAlbumWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Get Album Name")
        self.text_in = Entry(top_frame)
        self.labelResult = Label(top_frame, text="Result")
        self.labelInput.pack()
        self.text_in.pack()
        self.labelResult.pack()
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='active')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
        self.handleb.pack(side=LEFT)
                
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        album = self.text_in.get()
        muxGet = musicGet_Functions(True)
        result = muxGet.get_album(album)
        print("result is ",result)
        if result != ():
            albums = []
            idx = 0
            for i in result:
                print(i)
                albums.append((result[idx][0],result[idx][1],result[idx][2],result[idx][3],result[idx][4],result[idx][5],result[idx][6]))
                idx = idx + 1
            print("albums are ", albums)            
            output = albums
        else:
            output = album + " not found"
            print(output)
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  
