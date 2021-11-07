import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTA2NTQ5NzA0MDAxNzE2MjY1.YYaQNA.vyM7pjYSgXiaBkXOWNJK-p9_wow')


