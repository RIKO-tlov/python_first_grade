import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

#convert("L")を追加
def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L").resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x360")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
