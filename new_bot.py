import tkinter as tk
from tkinter import *
import shutil,os,sys,modules
sys.path.append('./')


register_win = Tk()
register_win.title('bot_mkr')
register_win.geometry('900x650')
register_win.configure(bg="black")
register_win.resizable(False, False)
register_name = StringVar()
register_ID = StringVar()
register_key = StringVar()
register_secret = StringVar()
register_token = StringVar()

  
def add_user():

    
    global register_name
    global register_token
    
      
    

    success = Toplevel()
    success.geometry("350x250")
    success.configure(bg="light green")
    success.title("Successfully created the bot")
    success.resizable(False, False)
    sop = tk.Button(success, text='Success', width=25, height=2,command=success.destroy,
                    bg="green", activebackground="light grey", relief=GROOVE)
    sop.place(relx=0.5, rely=0.5, anchor=CENTER)
      
      
    dirname=register_name.get()
    dirname2=dirname+r'\\''config.py'
    dirname3=dirname+r"\\""bot_file.py"
    diram=dirname+'\\auto_mod_config.py'
    dira=dirname+'\\log_config.py'
    try:
       # Create target Directory
        
        os.mkdir(dirname)
        s=open(dirname3, "w+")
        s.close()
        print(f"{modules.color.OKGREEN}bot " ,f'{modules.color.OKCYAN}', dirname ,f'{modules.color.OKGREEN}',  f" Created {modules.color.ENDC}") 
    except FileExistsError:
        print(f"{modules.color.OKGREEN}""updated",f'{modules.color.OKCYAN}',dirname,f'{modules.color.ENDC}')

    
    
    
    
    
    
    shutil.copy(r'teamplate\bot_teamplate.py',dirname3)
    file = open(dirname2, "w+")
    file.write('#general'+"\n"+'bot_name='+"\'"+register_name.get()+"\'"+"\n"+'bot_ID='+"\'"+register_ID.get()+"\'"+"\n"+'bot_key='+"\'"+register_key.get()+"\'"+"\n"+'bot_secret='+"\'"+register_secret.get()+"\'"+"\n"+'bot_token='+"\'"+str(register_token.get())+"\'"+"\n"+'#modules\n'+'automod='+str(auto_mod.get())+"\n"+'loging='+str(log.get())+"\n"+'audio='+str(audio.get())+"\n")
    file.close()
    if auto_mod.get()==1:
        file = open(diram, "w+")
        file.close()
    if log.get()==1:
        file = open(dira, "w+")
        file.close()
    
  

msg1 = tk.Label(register_win, text='NAME:', relief=GROOVE)
msg1.place(relx=0.2, rely=0.1, anchor=CENTER)

msg1 = tk.Label(register_win, text='APPLICATION/CLIENT ID:', relief=GROOVE)
msg1.place(relx=0.2, rely=0.2, anchor=CENTER)

msg1 = tk.Label(register_win, text='PUBLIC KEY:', relief=GROOVE)
msg1.place(relx=0.2, rely=0.3, anchor=CENTER)

msg1 = tk.Label(register_win, text='CLIENT SECRET:', relief=GROOVE)
msg1.place(relx=0.2, rely=0.4, anchor=CENTER)


msg3 = tk.Label(register_win, text='TOKEN:', relief=GROOVE)
msg3.place(relx=0.2, rely=0.6, anchor=CENTER)

user_name = Entry(register_win, relief=GROOVE, textvariable=register_name)
user_name.place(relx=0.6, rely=0.1, anchor=CENTER, width=300)
user_name = Entry(register_win, relief=GROOVE, textvariable=register_ID)
user_name.place(relx=0.6, rely=0.2, anchor=CENTER, width=300)
user_name = Entry(register_win, relief=GROOVE, textvariable=register_key)
user_name.place(relx=0.6, rely=0.3, anchor=CENTER, width=300)
user_name = Entry(register_win, relief=GROOVE, textvariable=register_secret)
user_name.place(relx=0.6, rely=0.4, anchor=CENTER, width=300)



token = Entry(register_win, textvariable=register_token, relief=GROOVE)
token.place(relx=0.6, rely=0.6, anchor=CENTER, width=300)

button = tk.Button(register_win, text='create', width=20, height=2,command=add_user,
                     activebackground="dark grey", activeforeground="red", relief=GROOVE)
button.place(relx=0.5, rely=0.8, anchor=CENTER)

auto_mod = IntVar()
Checkbutton(register_win, text="auto-mod", variable=auto_mod).grid(row=0, sticky=W)

log = IntVar()
Checkbutton(register_win, text="loging buged", variable=log).grid(row=1, sticky=W)

audio = IntVar()
Checkbutton(register_win, text="audio", variable=audio).grid(row=2, sticky=W)

var4 = IntVar()
Checkbutton(register_win, text="4", variable=var4).grid(row=3, sticky=W)

var5 = IntVar()
Checkbutton(register_win, text="5", variable=var5).grid(row=4, sticky=W)




  
stop = tk.Button(register_win, text='EXIT', width=20, command=register_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.3, rely=1, anchor=SE)
#----------------------------------------------


register_win.mainloop()