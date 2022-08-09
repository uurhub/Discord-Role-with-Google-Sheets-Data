from os import name
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import sqlite3



Bot = discord.Client()
@Bot.event

async def on_ready():
    print("ready")

# Goole Sheets Settings

@Bot.event
async def on_message(message):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("Google Sheets Document json file",scope) # You need to enter your Google Sheets Document json file name in here e.g: index.json
    
    client = gspread.authorize(creds)


    sheet = client.open("Google Sheets, Sheets name").sheet1   # You need to enter here your sheets name e.g: firstpage

    satir = sheet.col_values( ) # --> You need to enter column number which you want to scan data

    if message.author == Bot.user:
            return
   
#  Databse Settings

    vt = sqlite3.connect(' ') # --> Your database file name e.g: index.db 

    im = vt.cursor()

    im.execute("CREATE TABLE IF NOT EXISTS *HERE* (id BIGINT, mail type UNIQUE)") # You need to write your database name into *HERE* area

    im.execute("SELECT * FROM *HERE*")  # You need to write your database name into *HERE* area

    veriler = im.fetchall()

    vrl = (message.author.id,message.content.lower())

    if ("@" , "edu.tr" , ".com" in message.content.lower()):  # In this statement working for controlling mail addresses. Is mail have @ , edu.tr or .com variables.
        try:
            if (message.author.id , message.content.lower()) not in veriler:
                im.execute("INSERT INTO *HERE* Values(?,?)", vrl) # You need to write your database name into *HERE* area.
                vt.commit()                                       # If your mail addresses don't registered in your database; in this statement, your mail addresses will write in your database 
                vt.close()
                print("Database Record Success")
                
                for i in satir:
                        if message.content.lower() in satir:        # In this statement working for giving Discord roles to your member.
                            await message.add_reaction("✅")
                            role = discord.utils.get(message.guild.roles, name = " ")  # This 3 of role changeable. You can add 1 role too.
                            role1 = discord.utils.get(message.guild.roles, name = " ") # You need to write your Discord role to name the area. Discord role must be the same here as what you wrote or your code will not work.
                            role2 = discord.utils.get(message.guild.roles, name = " ")
                            await message.author.add_roles(role)
                            await message.author.add_roles(role1)
                            await message.author.remove_roles(role2)
                            pprint(i)
                            break
                        else:
                            await message.add_reaction("❌")
                            await message.author.send("There is no mail in the Google Sheets")
                            break
            elif (message.author.id , message.content.lower()) in veriler:
                
                print("starting to role assignment")    # If your mail addresses are registered in your database; this statement will work 

                
                for i in satir:
                    if message.content.lower() in satir:
                        await message.add_reaction("✅")
                        role = discord.utils.get(message.guild.roles, name = " ")   # You need to write your Discord role to name the area. Discord role must be the same here as what you wrote or your code will not work.
                        role1 = discord.utils.get(message.guild.roles, name = " ")
                        role2 = discord.utils.get(message.guild.roles, name = " ")
                        await message.author.add_roles(role)
                        await message.author.add_roles(role1)
                        await message.author.remove_roles(role2)
                        pprint(i)
                        break
                    else:
                        pass
                        break

            else:
                print("error")

        except sqlite3.IntegrityError:
            await message.add_reaction("❌")
            await message.author.send("You are entering another user's email address.")

    else:
        await message.add_reaction("❌")
        await message.author.send("@ or .com is not in your email.")    


Bot.run(" ") # Your Discord Bot Token must be written here.