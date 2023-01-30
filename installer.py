import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('discord.py[voice]')
install('requests')

import requests
from os import getcwd

url = "https://raw.githubusercontent.com/snowflake677/test/main/test.txt"
directory = getcwd()
filename = directory + 'test.txt'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)

