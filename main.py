import os
import ctypes
import threading
import discord
from discord.ext.commands import Bot
import glob

def changeWallpaper():
    #threading.Timer(5.0, changeWallpaper).start()
    img0 = r"C:\Users\Beroris\Desktop\h\1.jpg" # Set your own paths here but make sure the file formats are correct
    img1 = r"C:\Users\Beroris\Desktop\h\1.jpeg"
    img2 = r"C:\Users\Beroris\Desktop\h\1.png"

    if os.path.exists(img0):
        ctypes.windll.user32.SystemParametersInfoW(20,0,img0,0)
    elif os.path.exists(img1):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img1, 0)
    elif os.path.exists(img2):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img2, 0)
    changeWallpaper.counter +=1
    print('Changed: ' + str(changeWallpaper.counter))
changeWallpaper.counter = 0
changeWallpaper()




token = 'TOKEN'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = Bot(command_prefix='1', case_insensitive=False, intents=intents)
imagesPath = r'C:\Users\Beroris\Desktop\h\*'
filePath = r'C:\Users\Beroris\Desktop\h\1'
image_types = ["png", "jpeg", "gif", "jpg"]

@bot.event
async def on_ready():
    activity = discord.Game(name=" online ", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Ayoooooooo, we logged in as {0.user}".format(bot))


@bot.command()
async def set(ctx):
    # CLEAR IMAGES FIRST
    await ctx.send('Clearing...')
    files = glob.glob(imagesPath)  # GET FILES IN THE IMAGES FOLDER
    if not files:  # IF NO FILES THEN
        await ctx.send('The folder is empty!')
    else:
        num = 0
        for f in files:
            os.remove(f)  # REMOVE FILES
            num = num + 1
        await ctx.send('Cleared ' + str(num) + ' files in ' + str(imagesPath))

    # NOW SET THE IMAGE
    for attachment in ctx.message.attachments:  # FOR ATTACHMENTS IN THE MESSAGE
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            fileEXT = os.path.splitext(attachment.filename)[1]  # SPLIT TO GET THE FILE EXTENTION SO PIC(.PNG)
            await attachment.save(filePath + fileEXT)  # SAVE TO FILEPATH + ITS EXTENTION
            changeWallpaper()
            await ctx.send('Set Image!')
        else:
            await ctx.send('Failed, Please provide an image of format PNG, JPG, JPEG, GIF ')

bot.run(token)

