from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from os import listdir
from os.path import isfile, join
images_opened = []
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'white', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='PNGs to PDF', bg = 'white')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getFile ():
    global images_opened
    images_opened = []
    import_file_path = filedialog.askopenfilename()
    slice_index = [pos for pos, char in enumerate(import_file_path) if char == '/']
    dir_path = import_file_path[:slice_index[-1]]
    imgs = [f for f in listdir(dir_path) if f.endswith('.png')]
    def getOrder(img):
        order = img[-6:-4] if img[-6:-4].isdigit() else img[-5]
        return int(order)
    imgs_tuple = [ (img,getOrder(img)) for img in imgs]
    imgs_tuple_SR = sorted(imgs_tuple, key=lambda t: t[1])
    imgs_path = [join(dir_path,file) for file, i in imgs_tuple_SR]
    
    for i in imgs_path:
        im_t = Image.open(i)
        images_opened.append(im_t.convert('RGB'))

    print(str(len(images_opened)) + " images were saved \nClick Convert to PDF button")
        
    
browseButton = tk.Button(text="Select First File", command=getFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton)

def convertToPdf ():
    global images_opened
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    images_opened[0].save(export_file_path,save_all=True, append_images=images_opened[1:])
    print("Saved pdf file completely ")

saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='Exit Application',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
