#Bot to check for TOS bans and name changes
#made by Tozla7
#if you have any issues or questions add me on discord - retarded#0001

import os
import discord

#BOT client and intents
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#Replace with channel ID
channel_id = CHANNEL_ID

#check console to make sure you're logged into your bot
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_member_update(guild, user):
    if user.discriminator == "0000":
        channel = client.get_channel(channel_id)
        await channel.send(f"{user} has been TOS banned!")

@client.event       
async def on_user_update(before, after):
    if before.name != after.name:
        message = f"{before.name} has changed their name to {after.name}."
        channel = client.get_channel(channel_id)
        await channel.send(message)

#run ping command to make sure the bot is responding   
@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.content == "$ping":
        try:
            await message.channel.send("pong")
        except Exception as e:
            print(f"Error sending message: {e}")
    elif message.content.startswith("$pfp"):
        try:
            # Check if a user is mentioned
            if len(message.mentions) == 0:
                await message.channel.send("You need to mention a user.")
            else:
                mentioned_user = message.mentions[0]  # Get the first mentioned user
                await message.channel.send(mentioned_user.avatar.url)  # Send the URL of their profile picture
        except Exception as e:
            print(f"Error sending message: {e}")
    elif message.content == "$boost":
        try:
            server = message.guild
            boosts = server.premium_subscription_count
            boosters = [(member, member.premium_since) for member in server.members if member.premium_since is not None]
            
            if len(boosters) == 0:
                await message.channel.send("No one is currently boosting the server.")
            else:
                boost_info = "\n".join(f"{booster[0].name} ({booster[0].id}) - Boosting since: {booster[1]}" for booster in boosters)
                response = f"The server currently has {boosts} boosts.\nBoosters:\n{boost_info}"
                await message.channel.send(response)
        except Exception as e:
            print(f"Error sending message: {e}")
#Replace BOT_TOKEN with your bot token
client.run('BOT_TOKEN')
