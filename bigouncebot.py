import os
import discord
from dotenv import load_dotenv

#token = os.get_env("token")
token = os.environ.get("TOKEN")

class bigOunce(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        
        print(f'Message from {message.author}: {message.content}')
        
        if message.author == client.user:
            return

        if message.author == "<@228347925183332352>":
            await message.channel.send("Gay")

        if("<@228347925183332352>" in message.content):
            for number in range(5):
                await message.channel.send('<@228347925183332352>')
        
        if("<@732432789949120542>" in message.content):
            for number in range(5):
                await message.channel.send('<@732432789949120542>')

        if("/tagluke" in message.content):
            tagnumstring = ''.join(filter(str.isdigit, message.content))
            if(tagnumstring == ''):
                tagnum == 1
            else:
                tagnum == int(tagnumstring)
            if(tagnum < 1):
                tagnum = 1
            if(tagnum > 10):
                tagnum = 10
            for number in range(tagnum):
                await message.channel.send('<@340318963428884490>')

intents = discord.Intents.default()
intents.message_content = True

client = bigOunce(intents=intents)
client.run(token)
