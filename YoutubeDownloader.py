from asyncio import streams
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from pytube import YouTube, Playlist
import os

window = Tk()
window.title("Youtube Downloader")
window.geometry("720x360")
window.resizable(False, False)

#COLOR = "#635e5e"
#fenster["background"] = COLOR
SavePath = ""
OPTIONS = ["","Video", "Audio", "Playlist"]

variable = StringVar(window)
variable.set(OPTIONS[0])

variable2 = StringVar(window)

def setSavePath():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    savepath = filedialog.askdirectory(parent=window,initialdir=desktop,title='Please set a path')
    global SavePath
    SavePath = savepath
    SpeicherOrt_Text.config(text = "Path: " + SavePath)            

def Download():
    SelectionValue = variable.get()
    TypeValue = variable2.get()
    EntryValue = Eingabefeld.get()
    if SavePath:
        if SelectionValue == OPTIONS[1]: # Download Video fiie
            DownloadVideo(EntryValue)
        elif SelectionValue == OPTIONS[2]: # Download Audio fiie
            DownloadAudio(EntryValue)
        elif SelectionValue == OPTIONS[3]: # Download Playlist
            DownloadPlaylist(EntryValue)
        else: messagebox.showerror("Invalid Option", "Please choose a valid option") # Options[0] = empty
    else: messagebox.showerror("invalid path", "Please choose a valid save path") 

def DownloadVideo(EntryValue):
    if EntryValue:
        YouTube(EntryValue).streams.get_highest_resolution().download(SavePath)
        print("Video Download successful")
        print(YouTube.streams)
        messagebox.showinfo("Success!","Download was succesful") 
    else:
        messagebox.showerror("No URL found!", "Please set a valid URL")      

def DownloadAudio(EntryValue):
    if EntryValue:
        audio = YouTube(EntryValue).streams.filter(only_audio=True)
        print(audio)
        audio[0].download(SavePath)
        print("Audio Download successful")
        print(YouTube.streams)
        os.startfile(SavePath)
    else:
        messagebox.showerror("No URL found", "Please type in a valid URL")

def DownloadPlaylist(EntryValue):
    if EntryValue:
        playlist = Playlist(EntryValue)
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(SavePath)
        os.startfile(SavePath)
        print("Playlist Download successful")
    else:
        messagebox.showerror("No URL found", "Please type in a valid URL")

Textfeld = ttk.Label(window, text="Put URL in") 
Eingabefeld = ttk.Entry(window)
SelectionMenu = ttk.OptionMenu(window, variable, *OPTIONS)
Download_Button = ttk.Button(window, text = "Download", command = Download)
SpeicherOrt_Text = ttk.Label(window, text = "Path:")
SpeicherOrt_Text["anchor"] = W
SpeicherOrt_Button = ttk.Button(window, text = "Set output Path", command = setSavePath)

Textfeld.place(height = 20, width = 120, x = 175, y = 110)
Eingabefeld.place(height = 40, width = 200, x = 300, y = 100)
SelectionMenu.place(height = 40, width = 100, x = 530, y = 100)
Download_Button.place(height = 40, width = 100, x = 300, y = 180)
SpeicherOrt_Text.place(height = 20, width = 200, x = 260, y = 240)
SpeicherOrt_Button.place(height = 40, width = 150, x = 290, y = 280)

window.mainloop()