from tkinter import *
import pytube

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("D:\Youtube downloads")
        print("Done!1")
    except Exception as e:
        print(e)

root = Tk()
root.title("Youtube Video Downloader")

Label(root,text="Youtube Video Downloader",fg="red",font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(root,text="Please enter the video url",font=("Calibri",12)).grid(sticky=N,pady=15,row=1)
notif = Label(root,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)

url = StringVar()
Entry(root,width=50,textvariable=url).grid(sticky=N,row=2)

Button(root,width=50,text="Download",font=("Calibri",12),command=download).grid(sticky=N,row=3,pady=1)


root.mainloop()