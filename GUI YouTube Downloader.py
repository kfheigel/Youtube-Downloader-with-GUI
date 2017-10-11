from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import ttk
import pafy, os

'''
Remember to always have updated in command prompt:
pip install -U youtube-dl
and
pip install -U pafy
'''

# ********************** Functions *******************************

def about():
    messagebox.showinfo("About the program", "  YouTube Downloader \n\n               v0.1")

def contact():
    messagebox.showinfo("Contact", "If you need help, make any suggestions,\
                        \nplease contact me through this e-mail address: \
                        \n\nkrzysztof.heigel@gmail.com")
    
def entryDataValidation(website):
    youTubeURL = "https://www.youtube.com/"
    if website[0:23] == youTubeURL[0:23]:
        return True
    else:
        messagebox.showwarning("WRONG URL ERROR", "Warning!\
                                \nYou have entered wrong URL!\nPlease, try again.")
        return False
    
def progressBar (size, name, extension):
    progress = ttk.Progressbar(root, orient = "horizontal", length = 200, mode = "indeterminate")
    progress.grid(row = 4, columnspan = 2)
    progress.start()

def saveFileAs(pafyTitle):
        fileNameForWriting = asksaveasfilename(initialdir=r"C:\Users\Public\Music",
                                               #filetypes =(("Webm File", "*.webm"),("All Files","*.*")),
                                               initialfile = pafyTitle,
                                               title = "Choose a directory.")
        directory = os.path.split(fileNameForWriting)[0]
        return directory, fileNameForWriting
        
def buttonClick():
    for i in range(1):
        url = entry.get("1.0",END) #Change("1.0",'end-1c'), because we get our link from text widget, not entry

        if entryDataValidation(url) == False:
            break
        else:
            pass
        
        video = pafy.new(url)
        title = video.title
        filePath, fileName = saveFileAs(title) #getting the filepath to save in specific directory
        
        if varVideo.get() == 1:
            bestvideo = video.getbest(preftype="mp4", ftypestrict=False)
            bestvideo.download(quiet=True,
                               filepath = fileName + '.' + bestvideo.extension)

        if varMusic.get() == 1:
            bestaudio = video.getbestaudio(preftype = "m4a")
            ###################################
            fileSize = bestaudio.get_filesize()
            progressBar(fileSize, fileName, bestaudio.extension)
            ################################### https://www.youtube.com/watch?v=UiyDmqO59QE
            bestaudio.download(quiet=True,
                               filepath = fileName + '.' + bestaudio.extension)
            
            
            

        if varVideo.get() == 0 and varMusic.get()== 0:
            messagebox.showwarning("WARNING", "Warning!\nNone of the check boxes are ticked!\
            \nChoose one to download")

# ********************** Start of the GUI ************************

root = Tk()
root.title("YouTube Downloader")

# ********************** Size of the window **********************

root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(406, 140))

# ********************** Menu bar ********************************

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = subMenu)
subMenu.add_command(label = "About", command = about)
subMenu.add_command(label = "Contact", command = contact)

# ********************** Link entry ******************************

label = Label(root, text="Paste the youtube link: ")
label.grid(row = 0, sticky = W)

entry = Text(root, height = 1, width = 50, bd =2)
entry.grid(row = 1, columnspan = 2)

varVideo = IntVar()
varMusic = IntVar()
checkButtonVideo = Checkbutton(root, text= "Video", variable = varVideo)
checkButtonMusic = Checkbutton(root, text = "Music", variable = varMusic)

checkButtonVideo.grid(row = 2, column = 0, sticky = W)
checkButtonMusic.grid(row = 2, column = 1, sticky = W)

button = Button(root, height=1, width=10, text = "Download", command = buttonClick)
button.grid(row = 3, columnspan = 2)


# ********************** Status bar *****************************

'''statusbar = Label(root, text = "Created by K. Heigel", bd = 2, relief = SUNKEN, anchor = W) 
statusbar.pack()'''

root.mainloop()
