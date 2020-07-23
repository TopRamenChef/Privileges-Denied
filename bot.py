import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_update(before,after):
    user = -1
    target = 243194333883400192
    required_nick = "[ALL PRIVILEDGES DENIED]"
    if after.id == target and after.nick != required_nick:  
        await after.edit(nick=required_nick,reason="Changed nickname again")
        print("Dunking on user.")

os.environ['ShazBotToken'] = "<token>"
token = os.environ['ShazBotToken']
client.run(token)
