# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:20:08 2019

@author: xzero
"""

from tkinter import *  
from tkinter import ttk  
from tkinter.ttk import Combobox
import matplotlib as mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import matplotlib.backends.tkagg as tkagg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg


 
#df = pd.read_csv('https://bit.ly/2A2zkI6')

#def clicked():

    
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

    
  
window = Tk()  
window.title("Проект по питону")  
window.geometry('1000x550')  


tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

lf = LabelFrame(tab2, text='Plot Area') 
lf.place(x=500,y=10,height=500,width=450) 

lf2 = LabelFrame(tab2,text='Settings Area')
lf2.place(x=100,y=10,height=500,width=350)






 
menu = Menu(window)
new_item = Menu(menu)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)



tab_control.add(tab1, text='База данных')
tab_control.add(tab2, text='Отчеты')  
tab_control.pack(expand=1,fill='both')  

value = StringVar()
combo = Combobox(lf2, textvariable=value)  
lbl = Label(lf2 ,text='Выберите вид отчета:')
lbl.place(x=10,y=7,height=20,width=150)
combo['values'] = ("Столбчатая диаграмма(кач-кач)","Гистограмма(кол-кач)", "Диаграмма Бокса-Вискера(кол-кач)","Диаграмма рассеивания(2 кол - кач)")  
combo.current(0)  
combo.place(x=10,y=30, height=20, width=200)


canvas = Canvas(lf, width=1000, height=800 )
canvas.pack()



# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(1, 1))

#Задать размер рисунка примерно 11x12 см. но надо смотреть, как связано (а как-то связано) с параметрами размера
#в Canvas(lf, width=1000, height=800 )
fig.set_size_inches(11./2.54, 12.6/2.54)
ax = fig.add_axes([0, 0, 1, 1])

# Данные для примера (синусоида)
X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)

ax.plot(X, Y)


# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 1, 1
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()







def Build1():
    f=plt.Figure(figsize=(5,4),dpi=75)
    ax= f.add_subplot(111)

    data = (20, 35, 37 ,39 ,40)

    ind = np.arange(5)
    width= .5
    rects = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f , master=lf)
    canvas.draw()
    canvas.get_tk_widget().place(x=20,y=10,height=450,width=400)

def Build2():
    f=plt.Figure(figsize=(5,4),dpi=75)
    ax= f.add_subplot(111)

    data = (20, 35, 37 ,39 ,40)

    ind = np.arange(5)
    width= .5
    rects = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f , master=lf)
    canvas.draw()
    canvas.get_tk_widget().place(x=20,y=10,height=450,width=400)
    
def Build3(n,k):
    f=plt.Figure(figsize=(5,4),dpi=75)
    ax=f.subplots()
    ax.boxplot(k, patch_artist = True, medianprops = {'color': median_color}, boxprops = {'color': base_color, 'facecolor': base_color}, whiskerprops = {'color': base_color}, capprops = {'color': base_color})
    ax.set_xticklabels(n)
    ax.set_ylabel(k)
    ax.set_xlabel(n)
    ax.set_title(title)

    canvas = FigureCanvasTkAgg(ax , master=lf)
    canvas.draw()
    canvas.get_tk_widget().place(x=20,y=10,height=450,width=400)
    
def Build4():
    f=plt.Figure(figsize=(5,4),dpi=75)
    ax= f.add_subplot(111)

    data = (20, 35, 37 ,39 ,40)

    ind = np.arange(5)
    width= .5
    rects = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f , master=lf)
    canvas.draw()
    canvas.get_tk_widget().place(x=20,y=10,height=450,width=400)

       
        
        
        
def Click():
    if combo.get()=="Диаграмма рассеивания(2 кол - кач)":
        elem1 = Combobox(lf2)
        lbl1 = Label(lf2, text="Выберите количественный атрибут")
        lbl1.place(x=10, y=50, height=20, width=200)
        elem1['values']=("Частота","Цена","TDP","Объём кэша L3")
        elem1.current(0)
        elem1.place(x=10,y=73, height=20, width=200)
        lbl2 = Label(lf2, text="Выберите количественный атрибут")
        lbl2.place(x=10, y=93, height=20, width=200)
        elem2 = Combobox(lf2)
        elem2['values']=("Частота","Цена","TDP","Объём кэша L3")
        elem2.current(0)
        elem2.place(x=10,y=116, height=20,width=200)
        btn2 = Button(lf2, text='Построить',command=Build4)
        btn2.place(x=230, y=73, height=20, width=70)
        elem3 = Combobox(lf2)
        lbl3 = Label(lf2, text="Выберите качественный атрибут")
        lbl3.place(x=10, y=136, height=20, width=200)
        elem3['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem3.current(0)
        elem3.place(x=10,y=159, height=20,width=200) 
    if combo.get()=="Столбчатая диаграмма(кач-кач)":
        elem3 = Combobox(lf2)
        elem1 = Combobox(lf2)
        lbl1 = Label(lf2, text="Выберите качественный атрибут")
        lbl1.place(x=10, y=50, height=20, width=200)
        elem1['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem1.current(0)
        elem1.place(x=10,y=73, height=20, width=200)
        lbl2 = Label(lf2, text="Выберите качественный атрибут")
        lbl2.place(x=10, y=93, height=20, width=200)
        elem2 = Combobox(lf2)
        elem2['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem2.current(0)
        elem2.place(x=10,y=116, height=20,width=200)
        btn2 = Button(lf2, text='Построить',command=Build1)
        btn2.place(x=230, y=73, height=20, width=70)
        elem3 = Combobox(lf2)
        lbl3 = Label(lf2, text="Выберите качественный атрибут")
        lbl3.place(x=10, y=136, height=20, width=200)
        elem3['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem3.current(0)
        elem3.place(x=10,y=159, height=20,width=200)
        lbl3.destroy()
        elem3.destroy()
    if combo.get()=="Гистограмма(кол-кач)":
        elem1 = Combobox(lf2)
        lbl1 = Label(lf2, text="Выберите количественный атрибут")
        lbl1.place(x=10, y=50, height=20, width=200)
        elem1['values']=("Частота","Цена","TDP","Объём кэша L3")
        elem1.current(0)
        elem1.place(x=10,y=73, height=20, width=200)
        lbl2 = Label(lf2, text="Выберите качественный атрибут")
        lbl2.place(x=10, y=93, height=20, width=200)
        elem2 = Combobox(lf2)
        elem2['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem2.current(0)
        elem2.place(x=10,y=116, height=20,width=200)
        btn2 = Button(lf2, text='Построить',command=Build2)
        btn2.bind('<Button-1>')
        btn2.place(x=230, y=73, height=20, width=70)
        elem3 = Combobox(lf2)
        lbl3 = Label(lf2, text="Выберите качественный атрибут")
        lbl3.place(x=10, y=136, height=20, width=200)
        elem3['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem3.current(0)
        elem3.place(x=10,y=159, height=20,width=200)
        lbl3.place_forget()
        elem3.place_forget()
        n1=elem1.get()
        n2=elem2.get()
        print(n1,n2)
    if combo.get()=="Диаграмма Бокса-Вискера(кол-кач)":
        elem1 = Combobox(lf2)
        lbl1 = Label(lf2, text="Выберите количественный атрибут")
        lbl1.place(x=10, y=50, height=20, width=200)
        elem1['values']=("Частота","Цена","TDP","Объём кэша L3")
        elem1.current(0)
        elem1.place(x=10,y=73, height=20, width=200)
        lbl2 = Label(lf2, text="Выберите качественный атрибут")
        lbl2.place(x=10, y=93, height=20, width=200)
        elem2 = Combobox(lf2)
        elem2['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem2.current(0)
        elem2.place(x=10,y=116, height=20,width=200)
        n=elem1.get()
        k=elem2.get()
        btn2 = Button(lf2, text='Построить',command=Build3(n,k))
        btn2.place(x=230, y=73, height=20, width=70)
        elem3 = Combobox(lf2)
        lbl3 = Label(lf2, text="Выберите качественный атрибут")
        lbl3.place(x=10, y=136, height=20, width=200)
        elem3['values']=("Модель","Линейка","Socket","Ядро","Изготовитель","Техпроцесс")
        elem3.current(0)
        elem3.place(x=10,y=159, height=20,width=200)
        lbl3.place_forget()
        elem3.place_forget()
   
btn = Button(lf2, text='Выбрать',command=Click)
btn.place(x=230, y=30, height=20, width=70)



window.mainloop()