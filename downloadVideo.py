#############################################################################################
# Downloadify                                                                               #
#                                                                                           #
# By: Carson Spriggs-Audet                                                                  #
#                                                                                           #
# Date: 2021-08-10                                                                          #
#                                                                                           #
# Description: A very simple YouTube video downloader                                       #           
#        inspired by Victor Kamau's tutorial (source below).                                #
#############################################################################################

"""
Necessary pip installs:
pip install PyTube
pip install customtkinter
pip install Tkinter
"""

"""
Credits and Sources:

1. Tutorial for the foundation of the application:
   YouTube Video Downloader using Python by Victor Kamau
   Source: https://www.section.io/engineering-education/youtube-video-downloader-using-python/

2. Inspiration for enhancing the application's appearance:
   Modern GUI using Tkinter
   Source: https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22

   CustomTKinter Documentation
   Source: https://customtkinter.tomschimansky.com/documentation/color
"""


# Imports
import os
import tkinter as tk
import customtkinter
from tkinter import Label, Entry, StringVar, Button
from pytube import YouTube

customtkinter.set_default_color_theme("green") 

class Downloadify:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x250')
        self.root.resizable(True,True)
        self.root.title('Downloadify')
        self.link_var = StringVar()

        # Header text
        label_font = customtkinter.CTkFont(family='Inter', size=15, weight='bold')
        label = customtkinter.CTkLabel(self.root, text="Paste your chosen URL", font=label_font)
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # URL input box
        entry = customtkinter.CTkEntry(self.root, width=300, textvariable=self.link_var)
        entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        # File extension dropdown menu
        file_extension_label = customtkinter.CTkLabel(self.root, text="Select File Extension", font=label_font)
        file_extension_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Available file extensions
        file_extensions = ['mp4', 'webm']

        combobox = customtkinter.CTkComboBox(self.root, values=file_extensions)
        combobox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Save the combobox reference to access it later
        self.file_extension_combobox = combobox

        # Download button
        button_font = customtkinter.CTkFont(family='Inter', size=16, weight='bold')
        # On download button press, call the download function
        button = customtkinter.CTkButton(master=root, text='Download', font=button_font, command=self.download)
        button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


            
    def download(self):
            try:
                # Download the video using pytube
                url = YouTube(str(self.link_var.get()))

                # Get the selected file extension from the combobox
                selected_extension = self.file_extension_combobox.get()

                # Filter streams based on the selected file extension
                video = url.streams.filter(file_extension=selected_extension).first()

                # Place it in the downloads folder
                video.download(downloads_folder)

                # Success message
                label_font = customtkinter.CTkFont(family='Inter', size=15, weight='bold')
                label = customtkinter.CTkLabel(self.root, text="Done!", font=label_font)
                label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

            # Error caught (No URL inputted/Not a YouTube URL)
            except Exception as e:
                # Error message text display
                label_font = customtkinter.CTkFont(family='Inter', size=15, weight='bold')
                label = customtkinter.CTkLabel(self.root, text="Error, paste a valid YouTube URL", font=label_font)
                label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


# Find user's download folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Create the main window
root = customtkinter.CTk()
app = Downloadify(root)
root.mainloop()
