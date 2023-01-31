from logging import ERROR
import shutil,requests
import tkinter as tk
from tkinter import *
import os,sys,modules
sys.path.append('./')
register_win = Tk()
register_win.title('new.bot_mkr')
register_win.geometry('900x650')
register_win.configure(bg="black")
register_win.resizable(False, False)
register_name = StringVar()
register_ID = StringVar()
register_key = StringVar()
register_secret = StringVar()
register_token = StringVar()

  
def cb():
    
    dirname=register_name.get()
    dirname2=dirname+r'\\''config.py'
    dirname3=dirname+r"\\""bot_file.py"
    dirname4=dirname+r"\\""modules.py"
    try:
       # Create target Directory
        
        os.mkdir(dirname)
        
        print(f"{modules.color.OKGREEN}bot " ,f'{modules.color.OKCYAN}', dirname ,f'{modules.color.OKGREEN}',  f" Created {modules.color.ENDC}") 
    except FileExistsError:
        print(f"{modules.color.OKGREEN}""updated",f'{modules.color.OKCYAN}',dirname,f'{modules.color.ENDC}')
    f=open(dirname4,'w')
    f.write(requests.get("https://raw.githubusercontent.com/snowflake677/discord-bot-maker-python-/main/modules.py").content.decode())
    f.close()
    s=open(dirname3, "w")
    s.write(requests.get('https://raw.githubusercontent.com/snowflake677/discord-bot-maker-python-/main/teamplates/bot_teamplate.py').content.decode())
    s.close()
    file = open(dirname2, "w+")
    file.write('#general'+"\n"+'bot_name='+"\'"+register_name.get()+"\'"+"\n"+'bot_ID='+"\'"+register_ID.get()+"\'"+"\n"+'bot_key='+"\'"+register_key.get()+"\'"+"\n"+'bot_secret='+"\'"+register_secret.get()+"\'"+"\n"+'bot_token='+"\'"+str(register_token.get())+"\'"+"\n"+'#modules\n'+'automod=0'+"\n"+'loging=0'+"\n"+'audio=0'+"\n"+'chatGPT=0'+"\n"+'module5=0')
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

button = tk.Button(register_win, text='create', width=20, height=2,command=cb,
                     activebackground="dark grey", activeforeground="red", relief=GROOVE)
button.place(relx=0.5, rely=0.8, anchor=CENTER)






  
stop = tk.Button(register_win, text='EXIT', width=20, command=register_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.3, rely=1, anchor=SE)
#----------------------------------------------


register_win.mainloop()