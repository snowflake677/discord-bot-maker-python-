import tkinter as tk
from tkinter import *
import os,sys,modules
sys.path.append('./')


register_win = Tk()
register_win.title('bot_mkr')
register_win.geometry('900x650')
register_win.configure(bg="black")
register_win.resizable(False, False)
register_name = StringVar()
banned_words=StringVar()

  
def add_user():

    
    global register_name
    
    
      
    

    success = Toplevel()
    success.geometry("350x250")
    success.configure(bg="light green")
    success.title("Successfully created the bot")
    success.resizable(False, False)
    sop = tk.Button(success, text='Success', width=25, height=2,command=success.destroy,
                    bg="green", activebackground="light grey", relief=GROOVE)
    sop.place(relx=0.5, rely=0.5, anchor=CENTER)
      
      
    dirname=register_name.get()
    diram=dirname+'\\auto_mod_config.py'
    try:
        file = open(diram, "w+")
        file.write("\n"+'#auto mod' + "\n"+'blacklist = ["'+banned_words.get() + '"]')
        file.close()
        print(f"{modules.color.OKGREEN}""updated",f'{modules.color.OKCYAN}',dirname,f'{modules.color.ENDC}')
    except FileExistsError:
        print(f"{modules.color.FAIL}""bot.",f'{modules.color.OKCYAN}',dirname,f'{modules.color.FAIL}not found{modules.color.ENDC}')



    
  

msg1 = tk.Label(register_win, text='bot Name:', relief=GROOVE)
msg1.place(relx=0.5, rely=0.16, anchor=CENTER)


user_name = Entry(register_win, relief=GROOVE, textvariable=register_name)
user_name.place(relx=0.5, rely=0.2, anchor=CENTER, width=300)

bw = tk.Label(register_win, text='banned words(split with ,):', relief=GROOVE)
bw.place(relx=0.5, rely=0.26, anchor=CENTER)

bw2 = tk.Label(register_win, text='to ban all links add "http" as a banned word', relief=GROOVE)
bw2.place(relx=0.5, rely=0.34, anchor=CENTER)

b_w = Entry(register_win, relief=GROOVE, textvariable=banned_words)
b_w.place(relx=0.5, rely=0.3, anchor=CENTER, width=300)



button = tk.Button(register_win, text='create', width=20, height=2,command=add_user,
                     activebackground="dark grey", activeforeground="red", relief=GROOVE)
button.place(relx=0.5, rely=0.8, anchor=CENTER)






  
stop = tk.Button(register_win, text='EXIT', width=20, command=register_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.3, rely=1, anchor=SE)
#----------------------------------------------


register_win.mainloop()