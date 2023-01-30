from logging import ERROR
import shutil,requests
import tkinter as tk
from tkinter import *
import os,sys,modules
sys.path.append('./')

def newbot():
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
        try:
           # Create target Directory
            
            os.mkdir(dirname)
            s=open(dirname3, "w+")
            s.close()
            print(f"{modules.color.OKGREEN}bot " ,f'{modules.color.OKCYAN}', dirname ,f'{modules.color.OKGREEN}',  f" Created {modules.color.ENDC}") 
        except FileExistsError:
            print(f"{modules.color.OKGREEN}""updated",f'{modules.color.OKCYAN}',dirname,f'{modules.color.ENDC}')
    
        
        
        
        
        
        
        shutil.copy(requests.get('https://raw.githubusercontent.com/snowflake677/discord-bot-maker-python-/main/teamplates/bot_teamplate.py').content.decode(),dirname3)
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
config_win = Tk()
config_win.title('bot_mkr')
config_win.geometry('1400x1000')
config_win.configure(bg="black")
config_win.resizable(False, False)
bot_name = StringVar()
logc=StringVar()
banned_words=StringVar()
  
def update():

    
    global bot_name
    try:

        dirname=bot_name.get()
        diram=dirname+'\\config.py'
    
        file = open(diram, "w+")
        file.write("\n"+'#loging' + "\n"+'log_channel_ID = "'+logc.get() + '"\n')
        file.close()
        file.write("\n"+'#auto mod' + "\n"+'blacklist = ["'+banned_words.get() + '"]')
        file.close()
        print(f"{modules.color.OKGREEN}""updated",f'{modules.color.OKCYAN}',dirname,f'{modules.color.ENDC}')
        success = Toplevel()
        success.geometry("350x250")
        success.configure(bg="light green")
        success.title("Successfully created the bot")
        success.resizable(False, False)
        sop = tk.Button(success, text='Success', width=25, height=2,command=success.destroy,
                        bg="green", activebackground="light grey", relief=GROOVE)
        sop.place(relx=0.5, rely=0.5, anchor=CENTER)    
    except:
        print(f"{modules.color.FAIL}""bot",f'{modules.color.OKCYAN}',dirname,f'{modules.color.FAIL}not found{modules.color.ENDC}')



    
  

msg1 = tk.Label(config_win, text='bot Name:', relief=GROOVE)
msg1.place(relx=0.5, rely=0.16, anchor=CENTER)


user_name = Entry(config_win, relief=GROOVE, textvariable=bot_name)
user_name.place(relx=0.5, rely=0.2, anchor=CENTER, width=300)

bw = tk.Label(config_win, text='log config:', relief=GROOVE)
bw.place(relx=0.25, rely=0.16, anchor=CENTER)

bw = tk.Label(config_win, text='log channel ID:', relief=GROOVE)
bw.place(relx=0.25, rely=0.19, anchor=CENTER)

b_w = Entry(config_win, relief=GROOVE, textvariable=logc)
b_w.place(relx=0.25, rely=0.23, anchor=CENTER, width=300)


bw = tk.Label(config_win, text='automod config:', relief=GROOVE)
bw.place(relx=0.25, rely=0.34, anchor=CENTER)

bw = tk.Label(config_win, text='banned words(split with ,):', relief=GROOVE)
bw.place(relx=0.25, rely=0.38, anchor=CENTER)

bw2 = tk.Label(config_win, text='to ban all links add "http" as a banned word', relief=GROOVE)
bw2.place(relx=0.25, rely=0.46, anchor=CENTER)

b_w = Entry(config_win, relief=GROOVE, textvariable=banned_words)
b_w.place(relx=0.25, rely=0.42, anchor=CENTER, width=300)


bw = tk.Label(config_win, text='log config:', relief=GROOVE)
bw.place(relx=0.75, rely=0.16, anchor=CENTER)

bw = tk.Label(config_win, text='log channel ID:', relief=GROOVE)
bw.place(relx=0.75, rely=0.19, anchor=CENTER)

b_w = Entry(config_win, relief=GROOVE, textvariable=logc)
b_w.place(relx=0.75, rely=0.23, anchor=CENTER, width=300)


bw = tk.Label(config_win, text='automod config:', relief=GROOVE)
bw.place(relx=0.75, rely=0.34, anchor=CENTER)

bw = tk.Label(config_win, text='banned words(split with ,):', relief=GROOVE)
bw.place(relx=0.75, rely=0.38, anchor=CENTER)

bw2 = tk.Label(config_win, text='to ban all links add "http" as a banned word', relief=GROOVE)
bw2.place(relx=0.75, rely=0.46, anchor=CENTER)

b_w = Entry(config_win, relief=GROOVE, textvariable=banned_words)
b_w.place(relx=0.75, rely=0.42, anchor=CENTER, width=300)



#buttons
auto_mod = IntVar()
Checkbutton(config_win, text="enabled", variable=auto_mod).place(relx=0.33, rely=0.34, anchor=CENTER)

log = IntVar()
Checkbutton(config_win, text="enabled(buged)", variable=log).place(relx=0.33, rely=0.16, anchor=CENTER)

audio = IntVar()
Checkbutton(config_win, text="enabled", variable=audio).place(relx=0.83, rely=0.16, anchor=CENTER)

chatGPT = IntVar()
Checkbutton(config_win, text="enabled", variable=chatGPT).place(relx=0.83, rely=0.34, anchor=CENTER)

var5 = IntVar()
Checkbutton(config_win, text="enabled", variable=var5).place(relx=0.58, rely=0.34, anchor=CENTER)



tk.Button(config_win, text='new_bot', width=10, height=2,activebackground="dark grey", bg="red",relief=GROOVE,font=('system',10),command=newbot).grid(row=0, sticky=W)

button = tk.Button(config_win, text='update', width=20, height=2,command=update,
                     activebackground="dark grey", activeforeground="red",relief=GROOVE)
button.place(relx=0.5, rely=0.8, anchor=CENTER)






  
stop = tk.Button(config_win, text='EXIT', width=20, command=config_win.destroy,
                   bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.3, rely=1, anchor=SE)
#----------------------------------------------


config_win.mainloop()