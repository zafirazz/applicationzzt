import os
from tkinter import *
from PIL import ImageTk, Image

class App:
    def __init__(self, root, papka):
        self.papka = papka
        self.root = root
        self.root.geometry("700x600")
        p = os.getcwd()
        os.chdir(p + self.papka)
        p = os.getcwd()
        self.spisok = os.listdir(p)
        self.l = 0
        self.r = 1
        #lbls
        self.main_lbl = Label(self.root, text="Welcome to game THIS OR THAT!")
        self.im = Image.open(self.spisok[self.l])
        self.im = ImageTk.PhotoImage(self.im)
        self.im_lbl = Label(self.root, image=self.im)
        self.im_lbl.pack(side='left')
        self.imr = Image.open(self.spisok[self.r])
        self.imr = ImageTk.PhotoImage(self.imr)
        self.imr_lbl = Label(self.root, image=self.imr)
        self.imr_lbl.pack(side='right')
        #btns
        self.b1 = Button(self.root, text="left", command=self.left)
        self.b1.place(x=0, y=454)
        self.b2 = Button(self.root, text="right", command=self.right)
        self.b2.place(x=635, y=454)
        self.btn_new = Button(self.root, text='New', command=self.menu)
        self.btn_exit = Button(self.root, text='Exit', command=self.root.destroy)
        #txts
        self.win = Toplevel()
        self.txt = Text(self.root, height=20, width=80)
        self.txt_lbl = Label(self.root, text='Here is your #1 Book!')
        self.btn_books = Button(self.win, text='Еop books', command=self.top_book)
        self.win_label = Label(self.win, text="pick one", bg='black')

    def menu(self):
        self.win_label.pack(side='center')
        self.menubtn.pack(side='bottom')

    def top_book(self):
        self.papka = '/topbooks'
        self.l = 0
        self.r = 1
        self.left()
        self.right()

    def top_movie(self):
        pass

    def left(self):
        if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
            self.imr_lbl.after(1000, self.imr_lbl.destroy())
            self.b2.destroy()
            self.b1.destroy()
            self.im_lbl.pack(side='top')
            self.txt_lbl.pack(side='bottom')
            self.btn_new.pack(side='left')
            self.btn_exit.pack(side='right')

        if self.r < self.l:
            self.r = self.l + 1
            self.imr = Image.open(self.spisok[self.r])
            self.imr = ImageTk.PhotoImage(self.imr)
            self.imr_lbl.config(image=self.imr)
        else:
            self.r += 1
            self.imr = Image.open(self.spisok[self.r])
            self.imr = ImageTk.PhotoImage(self.imr)
            self.imr_lbl.config(image=self.imr)

    def right(self):
        if (self.r == (len(self.spisok) - 1) or self.l == (len(self.spisok) - 1)):
            self.im_lbl.after(1000, self.im_lbl.destroy())
            self.b1.destroy()
            self.b2.destroy()
            self.imr_lbl.pack(side='top')
            self.txt_lbl.pack(side='bottom')
            self.btn_new.pack(side='left')
            self.btn_exit.pack(side='right')

        if self.l < self.r:
            self.l = self.r + 1
            self.im = Image.open(self.spisok[self.l])
            self.im = ImageTk.PhotoImage(self.im)
            self.im_lbl.config(image=self.im)
        else:
            self.l += 1
            self.im = Image.open(self.spisok[self.l])
            self.im = ImageTk.PhotoImage(self.im)
            self.im_lbl.config(image=self.im)



root = Tk()
root.resizable(width=False, height=False)
ob = App(root, '/topbooks')
#game = Open(root)
##ob = App(root, '/topbooks')
root.mainloop()


#Pages with frames
# import tkinter as tk
# from PIL import ImageTk, Image
# import os
#
# LARGEFONT = ("Verdana", 35)
#
# class App(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#
#         container.grid_columnconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for f in (Menu, TopBooks, TopMovie):
#             frame = f(container, self)
#             self.frames[f]=frame
#             frame.grid(row=0, column=0, sticky='n')
#         self.open_frame(Menu)
#
#     def open_frame(self, controller):
#         frame = self.frames[controller]
#         frame.tkraise()
#
#
# class Menu(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         menu_lbl = tk.Label(self, text="Menu Page", font=LARGEFONT)
#         menu_lbl.pack(pady=40, padx=40)
#
#         btn1 = tk.Button(self, text="Top Books", command=lambda : controller.open_frame(TopBooks))
#         btn1.pack(side="bottom")
#         btn2 = tk.Button(self, text="Top Movies", command=lambda : controller.open_frame(TopMovie))
#         btn2.pack(side="bottom")
#
# class TopBooks(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         self.papka = "/top_books"
#         p = os.getcwd()
#         os.chdir(p + self.papka)
#         p = os.getcwd()
#         self.spisok = os.listdir(p)
#         l = 0
#         r = 1
#
#         bks_lbl = tk.Label(self, text="Pick only one!", font=LARGEFONT)
#         bks_lbl.pack(padx=50, pady=50)
#
#         im = tk.PhotoImage(file="/home/marbelle/PycharmProjects/intro_project/top_books/I-KISSED-SHARA-WHEELER-by-Casey-McQuiston.jpg")
#         tk.Label(image=im).pack(side='left')
#         btn_bks = tk.Button(self, text="Back to menu", command=lambda : controller.open_frame(Menu))
#         btn_bks.pack(padx=60, pady=60)
#
#
# class TopMovie(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         mvs_lbl = tk.Label(self, text="Pick only one!", font=LARGEFONT)
#         mvs_lbl.pack(padx=50, pady=50)
#
#         btn_mvs = tk.Button(self, text="Back to menu", command=lambda : controller.open_frame(Menu))
#         btn_mvs.pack(padx=60, pady=60)
#
# app = App()
# app.mainloop()








