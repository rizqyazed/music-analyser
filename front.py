from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import *
from librosa.core.notation import list_mela
from numpy.lib.function_base import insert
from index import *
from sqlite_engine import *
from lgn import *
from save import inject_data
import sys


## Window Properties
root = Tk() 
root.title("- {} logged in!".format(l_user.get()))
root.geometry("450x280+{}+{}".format(x_pos,y_pos))
root.config(bg="#131512")
root.resizable(False, False)


##Variables
TEXT = StringVar()

##Fucntions
"""Opens the dialog box"""
def open():
    """
    Args: None
    Return: Directory of the selected file
    """
    root.filename = filedialog.askopenfilename()
    print(root.filename)
    return root.filename

def inject(dir, bpm, key):
    if inject_data(dir, bpm, key):
        txt_box.insert(INSERT, "\nInjection Successfull!\nMetadata updated!!")
    return

"""Outputs the BPM and KEY of song"""
def fsend(dir):
    """
    Args: Directory of audio file
    Return: Outputs the BPM and KEY
    """
    global bpm, key
    bpm, key = analyse(dir)
    if bpm is None and key is None:
        txt_box.delete("1.0","end")
        txt_box.configure(fg="#00a7e5")
        return "Audio file unsupported..."
    else:
        txt_box.delete("1.0","end")
        txt_box.configure(fg="#00a7e5")
        return "BPM: " + str(round(bpm)) + "\nKEY: " + str(key) + "\n" 
        

## Widgets
#Frames
FrameTop = Frame(root, bg="#131512" )
FrameMid = Frame(root, bg="#131512")
FrameBottom = Frame(root,bg="#131512" )


#Entry
dir_value = Entry(FrameTop, 
                textvariable=TEXT, 
                bg="#171916", fg="#00a7e5",
                selectbackground = "#00a7e5", 
                width= 52, 
                highlightthickness=1, 
                insertborderwidth=0,
                highlightbackground="#00a7e5")


#Text Box
txt_box = ScrolledText(FrameMid, 
                    height = 10, width= 50, 
                    bg= "#171916", 
                    highlightthickness = 1,highlightbackground = "#00a7e5", 
                    selectbackground = "#00a7e5",
                    insertborderwidth = 0, 
                    fg="#9B9B9B")

txt_box.insert(INSERT, """##Press Load to open your desired audio file
                            \n##Then, hit send to analyse them
                            \n##The results should appear shortly after
                            \n##Inject only works with MP3 audio files""")

#Buttons
send = Button(FrameTop, 
            width= 5, height=1, 
            text="Send", 
            fg="#00a7e5", bg="#1d1f1c", 
            border= False, 
            command=lambda:txt_box.insert(INSERT,fsend(dir_value.get())))

load = Button(FrameTop, 
            width= 5, height=1, 
            text="Load", 
            fg="#00a7e5", bg="#1d1f1c", 
            border= False, 
            command=lambda:TEXT.set(open()))

inject = Button(FrameBottom, 
            width= 5, height=1, 
            text="Inject", 
            fg="#00a7e5", bg="#131512", 
            border= False,
            command= inject(dir_value.get(), round(bpm), str(key)) )

##Grid
send.grid(row=2, column=2, padx=(21,0))
load.grid(row=2, column=1)
dir_value.grid(row=2, column=0)
inject.grid(row=2,column=2)
txt_box.grid(row = 4 , column=0)

FrameTop.pack(padx= 10, pady=(10,5))
FrameMid.pack(pady=(5,0))
FrameBottom.pack(pady=(5,0),padx=(20),side= RIGHT)

## Final Stage-
conn.commit()
root.mainloop()
root.protocol("WM_DELETE_WINDOW", sys.exit("Program closed"))
conn.close()
print("Data Saved!")


