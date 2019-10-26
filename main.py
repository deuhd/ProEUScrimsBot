import discord
from discord.ext import commands
from discord.ext.commands import bot
import random

client = commands.Bot(command_prefix=".")

message_announcement = ""
general_manager_role_id = 543853681334943754
manager_role_id = 613425285001380027
moderator_role_id = 543871186489049118

@client.event
async def on_ready():
    activity = discord.Activity(name='PRO EU Scrims', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Im ready")

@client.event
async def on_member_join(member):
    print("DM Welcome sended.")
    embed = discord.Embed(color=discord.Color.red(),
                          description="Welcome to our PRO EU Scrim Discord Server! Please read the following rules and guidelines. By joining this server you have agreed to all of the rules listed below. Be respectful and courteous to everyone is part of this community.",
                          )

    embed.set_author(name="Welcome!",
                     icon_url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")

    embed.add_field(name="__**Rules**__:", value="**1. Spam**\n"
                                                 "Spam and flood messages is prohibited.\n"
                                                 "**2. Advertising**\n"
                                                 "Advertising streams, groups in socisl networks not related to the clan, links to website offering to buy or otherwise obtain in-game benefis is prohibited.\n"
                                                 "**3. Insultstt**\n"
                                                 "Any insults on the grounds of non-traditional sexual orientation, national or religious affiliatoion are prohibited.\n"
                                                 "**4. Avatar profile**\n"
                                                 "Use on your avatar profile obscene content is prohibited.\n"
                                                 "**5. Sale accounts**\n"
                                                 "The announcement of the sale/purchase of accounts and any other commercial activity is prohibited.", inline=False)
    embed.add_field(name="__**Follow us!**__:", value="Down below is all our social media.", inline=False)
    embed.add_field(name="__**Twitter:**__", value="[Click here to be redirected to our Twitter.](https://twitter.com/Proeupubgm)")
    embed.add_field(name="__**YouTube:**__", value="[Click here to be redirected to our YouTube.](https://www.youtube.com/channel/UCJsa5RLSC3sHtHcA7US8pww)")
    embed.add_field(name="__**Server:**__", value="Feel free to invite your friends to the server using this link: https://discord.gg/TsspjVh")
    await member.send(embed=embed)

message_id_for_reaction = 634043726788034586
role_gb = 633659766580838421
role_tr = 633675349611380736
role_ru = 633659602373967884

@client.event
async def on_raw_reaction_add(payload):
    print(payload.user_id)
    user_id = payload.user_id
    guild_id = payload.guild_id
    guild = await client.fetch_guild(guild_id)
    member = await guild.fetch_member(user_id)
    if payload.message_id == message_id_for_reaction:
        if payload.emoji.id == 634035682775531522:
            print("React gb")
            role = guild.get_role(role_gb)
            await member.add_roles(role)
        elif payload.emoji.id == 634037188174282782:
            print("React tr")
            role1 = guild.get_role(role_tr)
            await member.add_roles(role1)
        elif payload.emoji.id == 634037733173755924:
            print("React RU")
            role2 = guild.get_role(role_ru)
            await member.add_roles(role2)
        else:
            print("Cant find")

@client.event
async def on_raw_reaction_remove(payload):
    print(payload.user_id)
    user_id = payload.user_id
    guild_id = payload.guild_id
    guild = await client.fetch_guild(guild_id)
    member = await guild.fetch_member(user_id)
    if payload.message_id == message_id_for_reaction:
        if payload.emoji.id == 634035682775531522:
            print("unreact gb")
            role = guild.get_role(role_gb)
            await member.remove_roles(role)
        elif payload.emoji.id == 634037188174282782:
            print("unreact tr")
            role1 = guild.get_role(role_tr)
            await member.remove_roles(role1)
        elif payload.emoji.id == 634037733173755924:
            print("unreact RU")
            role2 = guild.get_role(role_ru)
            await member.remove_roles(role2)
        else:
            print("Cant find")



client.remove_command("help")

@client.command()
async def help(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Help command", icon_url=client.user.avatar_url)
        embed.set_thumbnail(url=client.user.avatar_url)

        embed.add_field(name="Command:", value="**.help**: Show all commands of this bot.\n"
                                               "**.write n (text)**: Type what you want the bot to send to the news channel.\n"
                                               "**.show n**: Show what the bot will write in the news channel.\n"
                                               "**.send n**: Send the message written in **.write (a/r)** to the news channel.\n"
                                               "**.image**: Send an image to the news channel.\n"
                                               "(Please DM **PrinhO** to put the image you want in the bot.)\n"
                                               "**.clear (amount)**: Clear messages.", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Help command:", icon_url=client.user.avatar_url)
        embed.set_thumbnail(url=client.user.avatar_url)

        embed.add_field(name="Commands:", value="**.ping**: Show how much ping you have.\n"
                                                "**.8ball**: Make decisions for you!", inline=False)

        await ctx.send(embed=embed)

def save_mod_write_in_announcement(announcement):
    global message_announcement
    if announcement is None:
        message_announcement = "None"
    else:
        message_announcement = announcement

@client.group()
async def write(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name="Invalid command", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Invalid write command passed", value="Please, use **.help** for more information.", inline=False)

            await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@write.command()
async def n(ctx, *, announcement):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        full_message = ctx.message.content
        full_message_list = full_message.split()
        announcement = " ".join(full_message_list[2:])
        print(announcement)
        save_mod_write_in_announcement(announcement)
        await ctx.send("Announcement saved! If you want to send in announcement channel use the command **.asend**.")
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.group()
async def show(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name="Invalid command", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Invalid show command passed", value="Please, use **.help** for more information.",
                            inline=False)

            await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@show.command()
async def n(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.send("Thats is what is gonna show if u use **.asend**:")
        await ctx.send(message_announcement)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.group()
async def send(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name="Invalid command", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Invalid send command passed", value="Please, use **.help** for more information.",
                            inline=False)

            await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@send.command()
async def n(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]
    announcement_send_text = client.get_channel(633315914212835338)

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.send("Message sent successfully.")
        await announcement_send_text.send(message_announcement)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command()
async def clear(ctx, *, amount : int):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command()
async def ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send("Pong! ``{}ms``".format(ping))

@client.group()
async def image(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid image command passed...')
            await ctx.send("Please, use **.help** for more information.")
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@image.command()
async def result(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]
    result_send_text = client.get_channel(603907089387225110)

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.send("Image sent successfully!")
        await result_send_text.send(file=discord.File('pro_eu_league_.png'))
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command()
async def p(ctx, *, text):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.channel.purge(limit=1)
        await ctx.send(text)
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command()
async def imgone(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.channel.purge(limit=1)
        await ctx.send(file=discord.File('image2.jpg'))
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command()
async def imgtwo(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids or moderator_role_id in list_of_author_role_ids:
        await ctx.channel.purge(limit=1)
        await ctx.send(file=discord.File('image1.jpg'))
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
        resposta = [
            "Outlook good.",
            "My sources say no.",
            "Most likely.",
            "Signs point to yes.",
            "My reply is no.",
            "Ask again later.",
            "Reply hazy, try again",
            "Don't count on it.",
            "Count on it.",
            "Yes :smile:",
            "No :slight_smile:",
        ]

        await ctx.send("Question: {}\nAnswer: {}".format(question, random.choice(resposta)))
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send("Not here man gang gang")

@client.group()
async def test(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids:
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid image command passed...')
            await ctx.send("Please, use **.help** for more information.")
    else:
        await ctx.send("Sorry, you don't have permission to use this command.")

@test.command()
async def eng(ctx):
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids:
        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Tournament rules", icon_url=client.user.avatar_url)
        embed.set_thumbnail(url=client.user.avatar_url)

        embed.add_field(name="Lol", value="By joining this server you have agreed to all of the rules listed below.", inline=False)

        await ctx.send(embed=embed)

@client.command()
async def teste(ctx):
    embed = discord.Embed(color=ctx.author.color,
                          description="Welcome to our PRO EU Scrim Discord Server! Please read the following rules and guidelines. By joining this server you have agreed to all of the rules listed below. Be respectful and courteous to everyone is part of this community.",
                          )

    embed.set_author(name="Welcome!",
                     icon_url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")

    embed.add_field(name="__**Rules**__:", value="**1. Spam**\n"
                                                 "Spam and flood messages is prohibited.\n"
                                                 "**2. Advertising**\n"
                                                 "Advertising streams, groups in socisl networks not related to the clan, links to website offering to buy or otherwise obtain in-game benefis is prohibited.\n"
                                                 "**3. Insults**\n"
                                                 "Any insults on the grounds of non-traditional sexual orientation, national or religious affiliatoion are prohibited.\n"
                                                 "**4. Avatar profile**\n"
                                                 "Use on your avatar profile obscene content is prohibited.\n"
                                                 "**5. Sale accounts**\n"
                                                 "The announcement of the sale/purchase of accounts and any other commercial activity is prohibited.", inline=False)
    embed.add_field(name="__**Follow us!**__:", value="Down below is all our social media.", inline=False)
    embed.add_field(name="__**Twitter:**__", value="[Click here to be redirected to our Twitter.](https://twitter.com/Proeupubgm)")
    embed.add_field(name="__**YouTube:**__", value="[Click here to be redirected to our YouTube.](https://www.youtube.com/channel/UCJsa5RLSC3sHtHcA7US8pww)")
    embed.add_field(name="__**Server:**__", value="Feel free to invite your friends to the server using this link: https://discord.gg/TsspjVh")
    await ctx.send(embed=embed)

@client.command()
async def msg(ctx):
    emoji_gb = "<:gb:634035682775531522>"
    emoji_tr = "<:tr:634037188174282782>"
    emoji_ru = "<:ru:634037733173755924>"
    emoji_pro_eu = "<:proeu:613291559013580810>"
    list_of_author_role_ids = [role.id for role in ctx.author.roles]

    if manager_role_id in list_of_author_role_ids or general_manager_role_id in list_of_author_role_ids:
        embed = discord.Embed(color=discord.Color.red())

        embed.set_author(name="PRO EU Scrim",
                         icon_url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/629651983032385538/633680180338098203/image0.png")

        embed.add_field(name="Select your language", value="Choose your language in the reactions below this message!\n\n"
                                                           "{} - English\n"
                                                           "{} - Russian\n"
                                                           "{} - Turkish\n\n"
                                                           "{}".format(emoji_gb, emoji_ru, emoji_tr, emoji_pro_eu), inline=False)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
