from print_graph import build_graph
from algorithm import *
from tkinter import *
import tkinter.messagebox as mb
import tkinter.filedialog as fl


def info_about_prog():
    msg="Данная программа принимает на вход значения в виде названий вершин, расположенных сверху вних в "\
        "зависимости от приоритета (параллельные значения задаются в одну строку). На выход идет граф приоритетов, " \
        "чтобы правильно увидеть приоритеты, граф должен быть направленным, для этого пользователю необходимо включить " \
        "флажок \'to\' в разделе edges/arrows"
    mb.showinfo("info", msg)

def make_graph():
    str = entry_field.get(1.0, END)
    set_of_nodes=create_list_of_nodes(str)
    build_graph(set_of_nodes)

def new_file():
    entry_field.delete(1.0, END)

def open_file():

    file=fl.askopenfilename(title="Открыть файл", initialdir='/')
    with open(file) as f:
        entry_field.insert(1.0, f.read())

def save_file():
    str = entry_field.get(1.0, END)
    new_file=fl.asksaveasfile(title="Сохранить файл", defaultextension=".txt")
    if new_file:
        new_file.write(str)
        new_file.close()


window = Tk()
window.title("Граф предпочтений")
window.geometry("400x350")
mainmenu = Menu(window)
window.config(menu=mainmenu)

nodes=Menu(mainmenu, tearoff=0)
nodes.add_command(label="new file", command=new_file)
nodes.add_command(label="open file", command=open_file)
nodes.add_command(label="save as", command=save_file)

mainmenu.add_cascade(label="file", menu=nodes)
mainmenu.add_cascade(label="info", command=info_about_prog)

label_top=Label(text="Поле для ввода выражения")
entry_field = Text(width=30,  height=17)
scroll = Scrollbar()
active_button=Button(text="Нарисовать граф", command=make_graph)

label_top.pack(anchor="center")
entry_field.pack(side="top" )
scroll.pack(side=RIGHT, fill=Y)
entry_field.config(yscrollcommand=scroll.set)
active_button.pack(pady=15)

window.mainloop()
