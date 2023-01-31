#import everything
import logging,logging.handlers,random,sys,modules,discord,config
import tkinter as tk
from datetime import datetime
from tkinter import font
from discord.ext import commands
from discord.ext.audiorec import NativeVoiceClient
from discord.utils import get

sys.path.append('./')



#setting up the bot
Bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='main.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)
@Bot.event
async def on_ready():
  await Bot.change_presence(activity=discord.Streaming(name='on {} servers.'.format(len(Bot.guilds)), url='https://www.twitch.tv/minyria'))
  print(f"{modules.color.OKGREEN}Bot Online!{modules.color.ENDC}")
  print("Name : {}".format(Bot.user.name))
  print('ID: {}'.format(Bot.user.id))
  print("bot is on {} servers".format(len(Bot.guilds)))
  print(r'invite me:https://discord.com/api/oauth2/authorize?client_id='+config.bot_ID+r'&permissions=8&scope=bot%20applications.commands')
#auto-mod(ONLY DELETES BANNED WORDS)
if config.automod==1:
  @Bot.event
  async def on_message(msg):
    if msg.author.bot:
      return
    if any(x in msg.content for x in config.blacklist):
        await msg.reply('message contains banned word')
        await msg.delete()
    await Bot.process_commands(msg)
#loging

if config.loging==1:
  print(f'{modules.color.WARNING}loging removed for my sanity{modules.color.ENDC}')



  
#definitions

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
def log(action):
  
  
  dirname2=config.bot_name+'\\manegment_commands.log'

  print("log file found")

  file = open(dirname2, "a+")
  file.write("<")
  file.write(date_time)
  file.write(">")
  file.write(action + "\n")
  file.close()




#commands
class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page,color=discord.Color.from_rgb(88,101,242),title='**help**')
            await destination.send(embed=emby)
Bot.help_command = NewHelpName()

#audio
if config.audio==1:
  @Bot.command()
  async def join(ctx: commands.Context):
      channel: discord.VoiceChannel = ctx.author.voice.channel
      if ctx.voice_client is not None:
          return await ctx.voice_client.move_to(channel)
      await channel.connect(cls=NativeVoiceClient)
  @Bot.command()
  async def leave(ctx):
      await ctx.voice_client.disconnect()
  @Bot.command()
  async def rec(ctx):
      ctx.voice_client.record(lambda e: print(f"Exception: {e}"))
      embedVar = discord.Embed(title="Started the Recording!",
                               description="use !stop to stop!", color=0x546e7a)
      await ctx.send(embed=embedVar)
  @Bot.command()
  async def stop(ctx: commands.Context):
      if not ctx.voice_client.is_recording():
          return
      await ctx.send(f'Stopping the Recording')
  
      wav_bytes = await ctx.voice_client.stop_record()
  
      name = str(random.randint(000000, 999999))
      with open(f'{name}.wav', 'wb') as f:
          f.write(wav_bytes)
          f.close()
      await ctx.voice_client.disconnect()
      
        

#other
@Bot.command()
@commands.is_owner() 
async def shutdown(ctx):
    log('shuting down via discord')
    await ctx.send("Bot shuting down")
    await ctx.send("disconeckting bot from host")
    print("<",date_time,"> shutdown command was run in discord")
    print("<",date_time,"> Bot shuting down")
    await ctx.send(':ballot_box_with_check:')
    await Bot.close()
@Bot.command()
async def ping(ctx):
    await ctx.send('pong')
@Bot.command()
async def test(ctx,member: discord.Member):
    await ctx.send('test')
    await member.send(content='test')
@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,reason:str="No reason"):
  await member.send(content=reason)
  await ctx.send(member,' was banned for ',reason)
  await member.ban(reason=reason)
@Bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member,reason:str="No reason"):
  await member.send(content=reason)
  await ctx.send(member,' was kicked for ',reason)
  await member.kick(reason=reason)

#keeping it alive
root=tk.Tk()
root.title('create bot')
root.geometry('900x650')

root.resizable(False, False)
counter = 3
def counter_label(label):
  
  def count():
    global counter
    counter -= 1
    label.config(text=str(counter))
    label.after(1000, count)
    if counter<=0:
      root.destroy()
  count()
font1=font.Font(size=30,family='system')
label = tk.Label(root, fg="red",font=font1)
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
counter_label(label)

button = tk.Button(root, text='  wait a bit for the bot to boot  ', width=20, height=2,
                     activebackground="dark grey", activeforeground="red", relief=tk.GROOVE,state="disabled",font=font1)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
root.mainloop()
Bot.run(config.bot_token,reconnect=False)