import discord
import asyncio
import random
import json

with open("config.json") as jsonfile:
    config = json.load(jsonfile)

client = discord.Client();
token = config['token'];
idmg = config['owner_id'];
cor = "B0F7F1";
user_id = None;
msg_id = None;

#Bot_Start

@client.event
async def on_ready():
    print("Bot online: ")
    print(client.user.name)
    print(client.user.id)
    print("-------IG-------")
@client.event
async def on_message(message):

#Test_Message

    if message.content == "-oi":
        await client.send_message(message.channel,"Vai se fuder seu cringie")
    if message.content == "-test":
        await client.send_message(message.channel,"Hur dur")  

#Coin_roll

    if message.content == "-moeda":
        if message.author.id == idmg:
            choice = random.randint(1,2)
            if choice == 1:
                await client.add_reaction(message, "😜")
            if choice == 2:
                await client.add_reaction(message, "👑")
        else:
            await client.send_message(message.channel, "Você não tem permissão sua thot")  

#Elo_Checker

    if message.content == "-elo":
        desc =discord.Embed(
            title="Escolha seu elo",
            colour=0xB0F7F1,
            description="- Bronze - 🥉\n"
                        "- Prata - 🥈\n"
                        "- Ouro - 🥇\n"
                        "- Plantina - 🔹\n"
                        "- Diamante - 💎\n"
                        "- Mestre - 🎓\n"
                        "- Desafiante - 🏆\n"
        )
        bot_msg = await client.send_message(message.channel, embed = desc)
        emoji_list = ["🥉", "🥈", "🥇", "🔹", "💎", "🎓", "🏆"]
        for emoji in emoji_list:
            await client.add_reaction(bot_msg, emoji)
            await asyncio.sleep(0.1)
        
    global msg_id
    msg_id = bot_msg.id
    global msg_user
    msg_user = message.author

#Role add(elo)

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    emoji_list = ["🥉", "🥈", "🥇", "🔹", "💎", "🎓", "🏆"]
    role_list = ["Bronze", "Prata", "Ouro", "Plantina", "Diamante", "Mestre", "Challenger"]
    for x in range(len(emoji_list)):
        if reaction.emoji == emoji_list[x] and msg.id == msg_id:
            role = discord.utils.get(msg.server.roles, name=role_list[x])
            await client.add_roles(user, role)
            print("add")
            break;

#Role_remove(elo)

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    emoji_list = ["🥉", "🥈", "🥇", "🔹", "💎", "🎓", "🏆"]
    role_list = ["Bronze", "Prata", "Ouro", "Plantina", "Diamante", "Mestre", "Challenger"]
    for x in range(len(emoji_list)):
        if reaction.emoji == emoji_list[x] and msg.id == msg_id:
            role = discord.utils.get(msg.server.roles, name=role_list[x])
            await client.remove_roles(user, role)
            print("remove")
            break;

client.run(token)
