import tkinter

def helloCallBack():
    print("Hello Call Back")

def create_window():
    window = tkinter.Tk()
    window.geometry("500x350")
    window.title("YouTube Downloader")

    download_frame = tkinter.Frame(window,pady=5)
    url_frame = tkinter.Frame(window,pady=5)

    download_label = tkinter.Label(download_frame,text="Download Options")
    download_choice = tkinter.StringVar(window)
    download_choice.set("Channel")
    download_menu = tkinter.OptionMenu(download_frame, download_choice,"Channel","Playlist","Video","Audio")
    url_label = tkinter.Label(url_frame,text="URL ")
    url_textbox = tkinter.Entry(url_frame, width = 40, borderwidth=1, background="yellow")
    download_button = tkinter.Button(window,text="Download",command=helloCallBack)

#    status_textbox = tkinter.Text(window, "Status",height=10, width = 40, pady=10)
#    status_textbox.tag_configure()

    download_label.pack(side=tkinter.LEFT)
    download_menu.pack(side=tkinter.LEFT)
    url_label.pack(side=tkinter.LEFT)
    url_textbox.pack(side=tkinter.LEFT)
    download_frame.pack()
    url_frame.pack()
    download_button.pack()
    url_textbox.focus()
#    status_textbox.pack()
    window.mainloop()