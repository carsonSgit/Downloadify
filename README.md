# Downloadify

## About

Downloadify is a GPU based Python Script inspired by Victor Kamau's ["Youtube Video Downloader using Python"](https://www.section.io/engineering-education/youtube-video-downloader-using-python/) tutorial.
Being new to Python, I wanted something simple that I could challenge myself by improving upon.

## Improvements

My improvements on Kamau's tutorial were primarily to bring the code up to the standard of what I have learnt while getting my Computer Science degree.
I made various improvements on to Kamau's code, added documentation, error handling & implemented another Python import, [CustomTKinter](https://customtkinter.tomschimansky.com/).

I found CustomTKinter through Fareed Khan's [blog post](https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22) on Medium, which gave me an introductory tutorial on how to use it.
I went through CustomTKinter's documentation and made more modifications to the original code so that the application looks a lot more Modern and fits a higher GUI standard.

### How to run

Download the script, and make sure you have all the pip installs necessary:

For the core of the Application, the plugin that allows you to download off of a YouTube URL:

```
pip install PyTube
```
Comes with Python, but just to cover all your bases, make sure the latest version of Tkinter is installed:
```
pip install Tkinter
```
Custom Tkinter, this is how the app is able to have a more modern GUI:
```
pip install customtkinter
```

### Run steps


First, locate the script in your terminal (I use Git Bash)

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/f435d6ad-90fa-4d40-a0f3-61e33d8f4c48)

Enter the following command:
```
python downloadVideo.py
```

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/52cfea3d-4ff9-4364-8262-ee50851f9f2c)

You should then see a new window pop up, this is Downloadify!

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/73e11457-3e8f-4c78-92c6-2ec24a447248)

Now, open up [YouTube](https://youtube.com) and make your way to a video you want to download.

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/76bec8b1-00f1-4769-b821-b92d43055793)

Then, copy the URL

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/8e53e75d-ac80-4cb8-94dd-6aa5879590e6)

Now we need to bring it into the entry box of Downloadify

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/2b46c548-2640-4065-aae2-ccb8d21989b3)

Simply click download, and you should be given a success message

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/45d8b7b8-049d-4095-84d5-4e08464f05c1)

Make your way over to your downloads folder and you should see it there

![image](https://github.com/carsonSgit/Downloadify/assets/92652800/f60d4cc3-5208-43ae-a11b-271853347636)





