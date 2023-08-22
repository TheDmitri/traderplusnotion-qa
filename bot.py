import discord
import responses

async def send_message(message, user_message):
    try:
        response = await responses.get_response(user_message)
        embed = discord.Embed(title=f'{user_message}', description=f"{response}", color=discord.Color.blue())
        await message.channel.send(embed=embed)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE0MzEwOTcyNTg0ODg4MzIwMA.GnQTDK.C-t38GZYCa3n1bIjLoS_rx_AwiicyAPohLdB8g'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        print('------')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        if('!' not in user_message):
            return

        if message.channel.id == 660168081171283972:
            await send_message(message, user_message)

    client.run(TOKEN)
