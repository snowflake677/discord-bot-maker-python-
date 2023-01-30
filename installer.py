import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('discord.py[voice]')
install('requests')
import requests
def makefile(file=str)
    f=open(file,'w')
    f.write(requests.get("https://raw.githubusercontent.com/snowflake677/discord-bot-maker-python-/main/"+file).content.decode())
    f.close()
makefile('modules.py')
makefile('dashboard.py')
