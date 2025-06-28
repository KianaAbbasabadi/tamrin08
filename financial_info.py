from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg 
from file_manager import *
from validator import *

data_list=read_from_file("data.dat")

def load_data(data_list):
  
   clear_btn_click()
   for data in data_list:
    table.insert("", END, values=data)




def reset_form():
   user_id.set(0) 
   amount.set(0)
   date.set("")
   time.set("")
   document_type()
   description.set("")

def table_selected(x):
   selected_info=table.item(table.focus())["values"]
   if selected_info :
      user_id.set(selected_info[0])
      amount.set(selected_info[1])
      date.set(selected_info[2])
      time.set(selected_info[3])
      document_type.set(selected_info[4])  
      description.set(selected_info[5]) 


def save_btn_click():
 financial=(user_id.get() , amount.get() , date.get(), time.get() , document_type.get() , description.get())
 erros=financail_validator(financial)
 if erros:
    msg.showerror("Errors" ,"\n".join (erros))
 else:
  msg.showinfo("saved" , "data saved")
  table.insert("" ,END , values=financial )
  data_list.append(financial)
  write_to_file("data.dat" , data_list)
  reset_form()

def edit_btn_click():
 financial=(user_id.get() , amount.get() , date.get(), time.get() , document_type.get() , description.get())
 selected_item = table.focus()
 erros=financail_validator(financial)
 if erros:
    msg.showerror("Errors" ,"\n".join (erros))
 else:
       
        table.item(selected_item, values=financial)
        reset_form()

def remove_btn_click(): 
  selected_item = table.focus()
  if selected_item:
        table.delete(selected_item)
        reset_form()

def clear_btn_click():
      for row in table.get_children():
       table.delete(row)




window=Tk()
window.geometry("600x430")
window.title("Financial info")

#id
Label(window , text="ID" ).place(x=10, y=20)
user_id=IntVar()
Entry(window , textvariable=user_id).place(x=100 , y=20)
#amount
Label(window , text="Amount").place(x=10 , y=60)
amount=IntVar()
Entry(window , textvariable=amount).place(x=100 , y=60)
#date 
Label(window , text="Date ").place(x=10 , y=100)
date=StringVar()
Entry(window , textvariable=date).place(x=100 , y=100)
#time
Label(window , text="Time").place(x=10, y=140)
time=StringVar()
Entry(window , textvariable=time).place(x= 100, y=140)
#document type
Label(window , text="Document type").place(x=10, y=180)
document_type=StringVar()
ttk.Combobox(window ,textvariable=document_type ,  values=["receive" , "pay" ] , state="readonly").place(x=100 , y=180 )
#description
Label(window , text="Description").place(x=10 , y=220)
description=StringVar()
Entry(window , textvariable=description).place(x=100 , y=220)

table=ttk.Treeview(window , columns=[1 , 2, 3 , 4, 5 , 6] , show="headings")

table.heading( 1 , text="ID")
table.heading(2 , text="Amount")
table.heading(3 , text="Date ")
table.heading(4 , text="time")
table.heading(5, text="Doument type")
table.heading(6 ,text=" Description")

table.column(1 , width=60)
table.column(2 , width=100)
table.column(3 , width=100)
table.column(4 , width=100)
table.column(5 , width=100)
table.column(6 , width=100)

table.place(x=270 , y=20)
table.bind("<<TreeviewSelect>>", table_selected)

Button(window , text="Save" ,width=6, command=save_btn_click).place(x=20 , y=250)
Button(window , text="Edit" ,width=6, command=edit_btn_click).place(x=100 , y=250)
Button(window , text="Remove" ,width=6, command=remove_btn_click).place(x=170  , y=250)
Button(window  , text="Clear"  ,width=6, command=clear_btn_click). place(x=100 , y=290)

load_data(data_list)






window.mainloop()