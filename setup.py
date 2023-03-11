import os
import json

print("WARNING Please enter a new EMPTY folder or risk data loss")
print("WARNING This program is in development, please use wisely")


folder = input("\n\nPlease enter the folder path where you want the images to be stores: ")
if os.path.exists(folder):
    print("Valid path entered.")
else:
    while(os.path.exists(folder) == False):
        folder = input("Invalid path entered, please retry.")
    print("Valid path entered.")

token = input("\nPlease enter your discord BOT token, you can get this at the discord developer portal: ")


config = {"folder": folder, "token": token}
with open("config.json","w") as f:
    json.dump(config,f)