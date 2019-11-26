#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/11/14

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from PIL import Image
import cv2 as cv
import ipdb

i = 0
class UI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.initWidgets()

    def initWidgets(self):

        Label(self.master, text="LR Picture:").grid(row=0, column=0, stick=NW)
        self.entry1 = ttk.Entry(self.master)
        self.entry1.grid(row=0, column=1, stick=NW)

        Label(self.master, text="Picture size:").place(x=0, y=30)
        self.entry2 = ttk.Entry(self.master)
        self.entry2.place(x=75, y=30)

        ttk.Button(self.master, text='选择图片', command=self.open_file).grid(row=0, column=2, stick=NW)

    def open_file(self):
        # 调用askopenfile方法获取单个打开的文件
        file_path = filedialog.askopenfilename(title='选择图片', filetypes=[("图片", "*.png"), ('图片', '*.pneg')], initialdir='../')
        self.entry1.delete(0, END)
        self.entry1.insert(0, file_path)
        self.Img = Image.open(file_path)
        self.img_Show()

    def img_Show(self):

        self.w = self.Img.width  # 图片的宽
        self.h = self.Img.height  # 图片的高

        self.entry2.delete(0, END)
        self.entry2.insert(0, (self.w, self.h))

        global img_png
        self.img_png = ImageTk.PhotoImage(self.Img)
        label_Img = Label(self.master, image=self.img_png)
        label_Img.grid(row=0, column=3, stick=NW)

        label_Img.bind("<MouseWheel>", self.processWheel)

    def processWheel(self, event):

        fx = 1.25
        fy = 1.25
        if event.delta > 0:
            self.Img = self.Img.resize((int(self.w * fx), int(self.h * fy)))

        elif event.delta < 0:
            if int(self.w * 0.25) > 0 and int(self.h * 0.25) > 0:
                self.Img = self.Img.resize((int(self.w * 0.25), int(self.h * 0.25)))
            else:
                print('The w and h of picture are less than 0')
                quit()

        self.neww = self.Img.width  # 图片的宽
        self.newh = self.Img.height  # 图片的高
        self.get_win_size()
        self.img_Show()

    def get_win_size(self):
        self.master.update()
        # ipdb.set_trace()
        # win_w = self.master.winfo_width()
        # win_h = self.master.winfo_height()
        self.master.geometry('%dx%d' % (299 + self.neww, 27 + self.newh))
        if (299 + self.neww) > 1366 and (27 + self.newh) > 715:
            self.master.geometry('%dx%d' % (1366, 27 + 715)) 
        self.master.resizable(0, 0)  # 防止用户调整尺寸

root = Tk()
root.title("Meta-SR")
UI(root)
root.mainloop()