import discord
import BotName as bt


class MyClient(discord.Client):
    
    async def on_ready(self):
        print('Logged on as', self.user)
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    

    # 傳送訊息
    async def on_message(self, message):
        # 設定 發出訊息的 channel
        channels = ['bot-test']
        
        if str(message.channel) in channels:
        # don't respond to ourselves
            if message.author == self.user:
                return
            
            if message.content == 'hi':
                await message.channel.send('{message.mention} 嗨(?')
            
            if message.content.startswith('大佬'):
                await message.channel.send('各位大神安安 !!')
                await message.channel.send('小弟我帶你們騷兩圈!!')
                # await message.channel.send(f'你是說我很 [ 牛逼 ] ?! {message.channel}')
                
            else:
                return
        
        
    # 歡迎新人
    async def on_member_join(self, member):
        print("join")
        guild = member.guild
        # if guild.system_channel is not None:
        to_send = f'歡迎 {member.mention} 來到 {guild.name} !! \U0001F61D \U0001F61D \n記得選擇你的身分組 ~'
        await guild.system_channel.send(to_send)
        
    
    
        
                

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(intents=intents)

client.run(bt.name1)