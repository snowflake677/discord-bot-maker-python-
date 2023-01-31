import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('discord.py[voice]')
install('requests')
import requests
def makefile(file=str):
<<<<<<< HEAD
    f=open(r'dbmp\\'+file,'w')
=======
    f=open(file,'w')
>>>>>>> ae650a3cfd5490e4078d8d6f3a077a771080f415
    f.write(requests.get("https://raw.githubusercontent.com/snowflake677/discord-bot-maker-python-/main/"+file).content.decode())
    f.close()

makefile('dashboard.py')
