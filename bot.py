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
    if after.id == target:  
        print("Dunking on user.")
        await after.edit(nick="[ALL PRIVILEDGES DENIED]",reason="Changed nickname again")

os.environ['ShazBotToken'] = "YOUR_TOKEN_HERE"
token = os.environ['ShazBotToken']
client.run(token)
