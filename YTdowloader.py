import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    try:
        yt = YouTube(entry_url.get())
        if file_type.get() == "MP4":
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        if file_type.get() == "MP3":
            filename = stream.default_filename
            mp3_filename = filename[:-4] + ".mp3"
            import moviepy.editor as mp
            video = mp.AudioFileClip(filename)
            video.write_audiofile(mp3_filename)
            status_label.config(text="Download complete! Saved as " + mp3_filename)
        else:
            status_label.config(text="Download complete! Saved as " + stream.default_filename)
    except:
        status_label.config(text="Error: " + str(Exception))

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_url = tk.Label(frame, text="Enter YouTube URL:")
label_url.grid(row=0, column=0, sticky="w")

entry_url = tk.Entry(frame, width=50)
entry_url.grid(row=0, column=1, padx=5)

label_file_type = tk.Label(frame, text="Select file type:")
label_file_type.grid(row=1, column=0, sticky="w")

file_type = tk.StringVar()
file_type.set("MP4")

file_type_menu = ttk.Combobox(frame, textvariable=file_type, values=["MP4", "MP3"])
file_type_menu.grid(row=1, column=1, padx=5)

download_button = tk.Button(frame, text="Download", command=download_video)
download_button.grid(row=2, columnspan=2, pady=5)

status_label = tk.Label(frame, text="")
status_label.grid(row=3, columnspan=2)

root.mainloop()
