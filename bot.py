import discord

client = discord.Client()
guild = 194588301678739456
me = 563516170938875935

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_update(before,after):
    user = -1
    target = 243194333883400192
    if after.id == target:  
       await after.edit(nick="[ALL PRIVILEDGES DENIED]",reason="Changed nickname again")


client.run('NTYzNTE2MTcwOTM4ODc1OTM1.Xw-RtQ.uY4zExVOnUB40Q_dK6RHJ1eD0nc')
