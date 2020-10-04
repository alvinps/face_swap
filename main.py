import tkinter as tk
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk


def swap_function():
    
    pho  = Image.open('test1.jpg')
    pho = pho.resize((250,250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(pho)
    l3_photo.configure(image= photo)
    l3_photo.image = photo

def source_face_select():
    newfile = filedialog.askopenfilename()
    pho  = Image.open(newfile)
    pho = pho.resize((150,150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(pho)
    l1_photo.configure(image= photo)
    l1_photo.image = photo

        

def dest_img_select():

    newfile = filedialog.askopenfilename()
    pho  = Image.open(newfile)
    pho = pho.resize((150,150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(pho)
    l2_photo.configure(image= photo)
    l2_photo.image = photo
        
    
def save_output():
    return True


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1080x720')
    root.title("Face Swap")
    text = tk.Label(root, text= "This is a demo app for the Face Swap")
    text.pack()
    frame = tk.Frame(root, relief=tk.RAISED)
    frame.pack(padx=10,pady =5)
    
    photopath1 = 'img.png'
    photopath2 = 'img.png'
    
    pho1  = Image.open(photopath1)
    pho1 = pho1.resize((150,150), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(pho1)
    pho2  = Image.open(photopath1)
    pho2 = pho2.resize((150,150), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(pho2)
        

    l1_photo = tk.Label(frame, image=photo1)   
    l1_photo.grid(row=0,column =0,padx=1)
    text1 = tk.Label(frame,text="Source Image")
    text1.grid(row=1,column =0)
    button1 = tk.Button(frame, text='Select an image',command = source_face_select)
    button1.grid(row=2,column =0)
    

    swap_img = tk.PhotoImage(file='swap.png')
    swap_button = tk.Button(frame, image= swap_img,command = swap_function)
    swap_button.grid(row=3,column =1)
    

    l2_photo = tk.Label(frame, image=photo2)
    l2_photo.grid(row=4,column =0)
    text2 = tk.Label(frame,text="Destination Image")
    text2.grid(row=5,column =0)
    button2 = tk.Button(frame, text='Select an image',command = dest_img_select)
    button2.grid(row=6,column =0)
    

    
    #Destination:
    destpath = 'img.png'
    dest  = Image.open(destpath)
    dest = dest.resize((250,250), Image.ANTIALIAS)
    dest_image = ImageTk.PhotoImage(dest)

    

    l3_photo = tk.Label(frame, image=dest_image)
    l3_photo.grid(row=3,column =3,padx=10)
    text3 = tk.Label(frame,text="Output Image")
    text3.grid(row=4,column =3,padx=10)
    button3 = tk.Button(frame, text='SAVE',command = save_output)
    button3.grid(row=5,column =3,padx=10)
        
    root.mainloop()
    